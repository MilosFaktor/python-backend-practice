import json


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": [
                    {"id": 1, "name": "Alice", "active": "true"},
                    {"id": 2, "name": "Bob", "active": "false"},
                ],
            }
        ),
    }
