from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9d28751ba04a269f2e240c92e08e67ff"
# Your Auth Token from twilio.com/console
auth_token = "80c1a3137b672dc7a8886f22c8940877"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17788874442",
    from_="+16047061287",
    body="Hello from Ron Burgondi?")

print(message.sid)
