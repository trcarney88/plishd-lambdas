import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    # Get exectution ARN from notifications database
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('notifications')
    response = table.get_item(
        Key={
            'email': event['email']
        }
        )
    
    arn = response['Item']['arn']
    
    # Stop the exectution of the step function associated with the recipient email
    client = boto3.client('stepfunctions')
    response = client.stop_execution(executionArn=arn, error="None", cause="Execution stopped by application.")
    
    # Delete email address out of notifications
    table.delete_item(Key={
        'email': event['email']
    })
    
    return {
        'statusCode': 200,
        'body': str(response['stopDate'])
    }
