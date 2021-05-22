from Eshop.settings import auth_token,account_sid

def send_otp(body,to):
    from twilio.rest import Client
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+91" + to,
        from_="+15125184011",
        body=body)

    print(message.sid)

def generate_otp():
    import math,random
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP += digits[math.floor(random.random()*10)]
    return OTP

