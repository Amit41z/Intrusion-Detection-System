from twilio.rest import Client

account_sid = 'ACff6ea4790b26fa4bdaecb528f48ce5e0'
auth_token = ''
client = Client(account_sid, auth_token)


def sendSms():
    message = client.messages.create(
        from_='+17605383485',
        body='Alert!!! Intrusion Detected',
        to='+919798549669'
    )

    print(message.sid)
