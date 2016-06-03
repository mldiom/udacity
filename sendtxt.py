from twilio.rest import TwilioRestClient

account_sid = "{{ ACc13d8ffc482eb244a9ccc8226a6a2439 }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{ 84248d84afa6836ca8ea43fc1e5cf994 }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+14042718361",    # Replace with your phone number
    from_="+16786083473") # Replace with your Twilio number

print(message.sid)
