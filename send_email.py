import smtplib,ssl

def send_mail(message):
    host="smtp.gmail.com"
    port=465
    username="[username@gmail.com]"
    password="[your app password]"
    receiver=username
    context= ssl.create_default_context()
    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
