import json

def lambda_handler(event, context):
    print("Your lambda was triggered big dog!!")
    print("Event:", json.dumps(event))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }