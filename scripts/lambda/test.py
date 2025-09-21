import json

def lambda_handler(event, context):
    # Example: simple echo function
    print("Received event:", json.dumps(event))

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello from Lambda!", "input": event})
    }
