import json
import boto3
import os
from botocore.exceptions import ClientError


table_name = os.getenv("TABLE_NAME")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    method = event.get("httpMethod")
    body = json.loads(event.get("body"))
    headers = event.get("headers")
    idempotency_key = headers.get("Idempotency-Key")

    if not method == "POST":
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Wrong method, must be only POST"}),
        }

    try:
        resp = table.put_item(
            Item={"request_id": idempotency_key, "body": json.dumps(body)},
            ConditionExpression="attribute_not_exists(request_id)",
        )
        print(resp)
        return {"statusCode": 200, "body": json.dumps({"message": "Request processed"})}

    except ClientError as e:
        error_code = e.response["Error"]["Code"]

        if error_code == "ConditionalCheckFailedException":
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Duplicate request"}),
            }

        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
