# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
#this code you will get from twilio website 
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACe84190ddd9f6e177069c7fef164b8b53"
auth_token = "87a2b7a59e69ab6fb85853622e31ce2c"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+919505514559", 
    from_="+13607039801", # this is your twilio phone number ,can find this in your twilio account phone numbers
    body="Hello there! it is")
