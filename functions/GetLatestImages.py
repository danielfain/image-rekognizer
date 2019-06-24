import boto3
import json

dynamodb = boto3.resource('dynamodb', 'us-east-1')

def handler(event, context):
    table = dynamodb.Table('imgur_clone_images')
    limit = event['queryStringParameters']['limit']
    
    response = table.scan(
        Limit=int(limit),
        Select='ALL_ATTRIBUTES'
    )
    
    response = {
        "statusCode": 200,
        "body": json.dumps(response['Items']),
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
    }
    
    return response