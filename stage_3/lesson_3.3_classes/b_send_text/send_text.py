# Lesson 3.3: Use Classes
# Mini-Project: Send Text

# It can be important for businesses to automate sending
# text messages. In this mini-project we'll uses classes
# to send a text message using Twilio, a library we'll
# download from the Internet and add to Python.

from twilio.rest import Client

# Your code here.

# Your Account SID from twilio.com/console
account_sid = "ACeefc945ce545d8724afcf01b0bd88230"
# Your Auth Token from twilio.com/console
auth_token  = "4e9b3ffeabc1c8bda6e5686523cee1bf"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+6285729977530",
    from_="+6285574677326",
    body="Hello from Python!")

print(message.sid)
