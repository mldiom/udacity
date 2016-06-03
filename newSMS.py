from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACc13d8ffc482eb244a9ccc8226a6a2439" 
AUTH_TOKEN = "84248d84afa6836ca8ea43fc1e5cf994" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to="+14042718361", 
	from_="+16786083473", 
	body="sup dude",  
)
