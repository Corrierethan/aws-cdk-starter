import json


def handler(event, context):
    """Entry point for the hello Lambda function."""
    print("Lambda triggered.")
    print("Event:", json.dumps(event))

    return {
        "statusCode": 200,
        "body": json.dumps("Hello from Lambda!"),
    }