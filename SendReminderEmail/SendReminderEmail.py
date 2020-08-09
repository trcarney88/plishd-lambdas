import json
import arrow
import boto3
from botocore.exceptions import ClientError
from botocore.vendored import requests

SENDER = "Plishd <noreply@plishd.com>"

def email_reminder_handler(event, context):
    print(event)
    CHARSET = "UTF-8"
    client = boto3.client('ses', region_name="us-west-2")

    email_html = ''

    with open("./update-email-template.html", "r") as f:
        email_html = f.read()

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    event["email"]
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': 'Add an accomplishment now. www.plishd.com'
                    },
                    'Html': {
                        'Charset': CHARSET,
                        'Data': email_html
                    }
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': 'Plishd Notification: Update Accomplishments'
                }
            },
            Source = SENDER
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
        
    # Schedule next notification
    wait = getWaitTime(event['time'], event['waitTime'], event['interval'])
    
    return {
        'waitTime': wait,
        'email': event['email'],
        'interval': event['interval'],
        'time': event['time'],
        'continue': True
    }
    
def getWaitTime(time, reminderTime, interval):
    time = arrow.get(time, "HH:mm:SS")
    
    d = arrow.get(reminderTime)
    
    q1 = d.replace(month=4, day=1)
    q2 = d.replace(month=7, day=1)
    q3 = d.replace(month=10, day=1)
    q4 = d.replace(month=1, day=1, year=d.year + 1)

    if interval == 'D':
            d = d.shift(days=1)
    elif interval == 'W':
        d = d.shift(weeks=1)
    elif interval == 'M':
        d = d.shift(months=1)
    elif interval == 'Q':
        if d < q1:
            d = q1
        elif d < q2:
            d = q2
        elif d < q3:
            d = q3
        else:
            d = q4
    elif interval == 'SA':
        if d < q2:
            d = q2
        else:
            d = q4
    else:
        d = q4

    d = d.replace(hour=time.hour, minute=time.minute, second=0, microsecond=0)
    
    ret = d.for_json()
    
    return ret