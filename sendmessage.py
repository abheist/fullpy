from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "here comes twilio account sid..replace with yours"
auth_token  = "here comes auth_token, replace with yours.."
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
	body="My name is lol",
    to="+919761250893",    # Replace with your phone number
    from_="+12017302952") # Replace with your Twilio number
print message.sid