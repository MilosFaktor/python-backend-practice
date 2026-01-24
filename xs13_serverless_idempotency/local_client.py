import requests
import time
from dotenv import load_dotenv
import os
import uuid

"""XS13 - HTTP ingest + validation + idempotent write

Goal:
- Practice requests (GET + POST)
- Validate & normalize external JSON
- Implement idempotency using DynamoDB conditional writes
- Run everything locally with SAM + DynamoDB Local

Non-goals:
- SQS
- Scaling
- Production hardening"""


env_file = os.getenv("ENV", "local")  # default to local
load_dotenv(f".env.{env_file}")
api_url_get = os.getenv("URL_GET")
api_url_post = os.getenv("URL_POST")
timeout = float(os.getenv("TIMEOUT", "5"))


def fetch_users(url, timeout):
    status = (None, None)
    req_id = str(uuid.uuid4())
    for attempt in range(3):
        try:
            r = requests.get(url, timeout=timeout)

            if r.status_code != 200:
                status = (r.status_code, "status code failed")
                time.sleep(2**attempt)
                continue

            ### on success, status_code: 200
            return r.json(), (r.status_code, None)

        except Exception:
            status = (502, "upstream service unavailable")
            time.sleep(2**attempt)

    return {}, status


def clean_and_validate_response(users):

    if not users:
        return (
            [],
            (400, "Bad request(ValueError): 'users' is empty"),
        )

    if not isinstance(users, dict):
        return [], (400, "Bad request(TypeError): 'users' must be a dictionary")

    message = users.get("message")
    if not message:
        return [], (400, "Bad request(ValueError): 'message' is empty")

    if not isinstance(message, list):
        return [], (400, "Bad request(TypeError): 'message' must be a list")

    validated = []

    for row in message:
        if not row:
            continue
        if not isinstance(row, dict):
            continue

        new_row = dict(row)

        # id section
        if "id" not in row:
            continue
        id = row.get("id")
        if id is None:
            continue
        if isinstance(id, bool):
            continue
        elif isinstance(id, int):
            if not id >= 0:
                continue
            new_id = int(id)
            new_row["id"] = new_id
        elif isinstance(id, str):
            s = id.strip()
            if not s.isdigit():
                continue
            new_id = int(s)
            new_row["id"] = new_id
        else:
            continue

        # name section
        if "name" not in row:
            continue
        name = row.get("name")
        if not isinstance(name, str):
            continue
        s = name.strip()
        if not s:
            continue
        new_name = str(s)
        new_row["name"] = new_name

        # active section
        if "active" not in row:
            continue
        active = row.get("active")
        if isinstance(active, bool):
            new_active = active
        elif isinstance(active, str):
            s = active.strip().lower()
            if s not in ("true", "false"):
                continue
            new_active = s == "true"
        else:
            continue
        new_row["active"] = new_active

        validated.append(new_row)

    if not validated:
        return [], (400, "Bad request(ValueError): 'validated' is empty")

    return validated, (200, None)


def get_active_users(cleaned_users):
    if not isinstance(cleaned_users, list):
        return [], (400, "Bad request(TypeError): 'cleaned_users' must be a list")
    if not cleaned_users:
        return [], (400, "Bad request(ValueError): 'cleaned_users' is empty")

    active_users = []
    for u in cleaned_users:
        if u.get("active") is True:
            active_users.append(u)

    if not active_users:
        return [], (400, "Bad request(ValueError): 'active_users' is empty")

    return active_users, (200, None)


def build_output(active_users, status):
    status_code, error = status

    if status_code != 200:
        output = {
            "statusCode": status_code,
            "error": error,
        }

    else:
        output = {
            "statusCode": status_code,
            "count": len(active_users),
            "users": [],
        }

        for u in active_users:
            n_id = int(u.get("id"))
            n_name = str(u.get("name"))
            user = {
                "id": n_id,
                "name": n_name,
            }
            output["users"].append(user)

    return output


def write_output_to_dynamodb(url, output, timeout):
    status = (None, None)
    req_id = str(uuid.uuid4())
    headers = {
        "Idempotency-Key": req_id,
        "X-Request-Id": req_id,
    }
    for attempt in range(3):
        try:
            r = requests.post(url, headers=headers, json=output, timeout=timeout)

            if r.status_code != 200:
                status = (r.status_code, "status code failed")
                time.sleep(2**attempt)
                continue

            ### on success, status_code: 200
            return r.json(), (r.status_code, None)

        except Exception:
            status = (502, "upstream service unavailable")
            time.sleep(2**attempt)

    return {}, status


def main():

    input_users, i_status = fetch_users(api_url_get, timeout)
    if not i_status[1]:
        validated, v_status = clean_and_validate_response(input_users)
        if not v_status[1]:
            active_users, a_status = get_active_users(validated)
            output = build_output(active_users, a_status)
            if not a_status[1]:
                response = write_output_to_dynamodb(
                    api_url_post, output, timeout=timeout
                )
                print(response)

            else:
                print("error in new code. 'developing'")

        else:
            output = build_output(validated, v_status)  # build output on error
            print(output)

    else:
        output = build_output(input_users, i_status)  # build output on error
        print(output)


if __name__ == "__main__":
    main()
