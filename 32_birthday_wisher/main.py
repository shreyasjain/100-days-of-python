import smtplib

MY_EMAIL = "13sjain4ur7@gmail.com"
MY_PASSWORD = "kdja tdlq xzkv dsvi"
HOSTNAME = "smtp.gmail.com"

receiver_email = "shreyasjain4all@gmail.com"
message = "Subject: Testing\n\nHello there"

# connection = smtplib.SMTP(HOSTNAME)
# connection.starttls()
# connection.login(user=MY_EMAIL, password=MY_PASSWORD)
# connection.sendmail(from_addr=MY_EMAIL, to_addrs=receiver_email, msg=message)
# connection.close()

with smtplib.SMTP(HOSTNAME) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=receiver_email, msg=message)