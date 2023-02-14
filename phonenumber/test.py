from twilio.rest import Client

# Your Account SID from twilio.com/console
#account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
#auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+94767101263", 
    from_="(+94774459054)",
    body="Hello from Python!")

print(message.sid)