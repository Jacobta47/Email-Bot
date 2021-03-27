#*****************************************************************
#JACOB T. ARMENTROUT *********************************************
#*****************************************************************

import os
import time
import email
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()
host = os.getenv('host')
port = os.getenv('port')
sender = os.getenv('sender')
password = os.getenv('password')
reciever = os.getenv('reciever')
subject  = os.getenv('subject')
message = os.getenv('message')

login = sender

initial = 0

mail = smtplib.SMTP(host, port)
mail.ehlo()
mail.starttls()
mail.login(login, password)

def send():   
    mail.sendmail(sender, reciever, message)

while initial < 100:
    send()
    initial += 1
    print(initial)

print("done")

mail.close()
