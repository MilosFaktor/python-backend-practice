# main.py

from xs14.ingest import read_json_file
from xs14.validate import validate_raw
from xs14.transform import get_active_users
from xs14.output import build_success, build_error

# from xs14.validate import

json_path = "data/users_raw.json"
result = read_json_file(json_path)

validated = validate_raw(result)

transformed = get_active_users(validated)
for us in transformed:
    print(us)
