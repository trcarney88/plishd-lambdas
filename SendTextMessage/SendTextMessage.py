import json
import arrow
from twilio.rest import Client

SENDER = "+17753604775"
SID = "ACeba3e5e1a2af0083f4bb8b2d444a3193"
AUTH = "ada9b7ba33d948712b22a97f2158cf75"

def send_text_handler(event, context):
    client = Client(SID, AUTH)
    try:
        message = client.messages.create(
            from_=SENDER,
            body="Add an accomplishment! www.plishd.com/timeline/accomplishment/new/",
            to=event['mobile']
        )

        error_code = message.error_code
        error_message = message.error_message
        status = message.status
    except Exception as e:
        error_code = True
        error_message = str(e)
        status = "Exception Thrown"

    if error_code:
        print("Error: " + error_message)
    
    print("Message Status: " + status)
    
        
    # Schedule next notification
    wait = getWaitTime(event['time'], event['waitTime'], event['interval'])
    
    return {
        'waitTime': wait,
        'mobile': event['mobile'],
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
