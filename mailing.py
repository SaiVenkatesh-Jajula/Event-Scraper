import ssl,smtplib

def mailing(information):
    host="smtp.gmail.com"
    port=465
    context = ssl.create_default_context()

    username="saivenkatesh619@gmail.com"
    password = 'lfzwbmpcwxtasafu'
    send_to = 'saivenkatesh619@gmail.com'

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,send_to,information)

