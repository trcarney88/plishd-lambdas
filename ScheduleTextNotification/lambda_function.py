import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Invoke a step function to send the notification email at the proper time
    client = boto3.client('stepfunctions')
    response = client.start_execution(stateMachineArn='arn:aws:states:us-west-2:784692787615:stateMachine:Send_Text', input = json.dumps(event))
    arn = response['executionArn']
    
    # Save the execution ARN to a database so it can be deleted if necessary
    # I created the notifications db when there were just emails so email == mobile number in this case
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('notifications')
    response = table.query(KeyConditionExpression=Key('email').eq(event['mobile']))
    
    if len(response['Items']) == 0:
        table.put_item(Item={
            'email': event['mobile'],
            'arn': arn,
        })
    else:
        table.update_item(Key={
            'email': event['mobile'],
        },
        UpdateExpression='SET arn = :arn',
        ExpressionAttributeValues={
            ':arn':arn
        })
        
    return {
        'statusCode': 200,
        'body': arn
    }