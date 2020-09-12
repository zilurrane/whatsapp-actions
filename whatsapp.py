import os
from twilio.rest import Client

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
from_number = os.environ['from_number']
to_number = os.environ['to_number']
message = os.environ['message']

if from_number is None:
    from_number = '+14155238886'

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body=message,
                              from_='whatsapp:'+from_number,
                              to='whatsapp:'+os.environ['to_number']
                          )
