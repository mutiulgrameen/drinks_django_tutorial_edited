# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC2b85512e7cf7f0f2834011363d7a8109']
auth_token = os.environ['9b24e1895c264fec1d988a425bfcb3f4']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+8801521517554'
                          )

print(message.sid)