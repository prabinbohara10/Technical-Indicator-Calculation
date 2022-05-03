from email import message
import requests
from bs4 import BeautifulSoup
import time
import  smtplib,ssl



    

while 1==1:

    message="hi prabin"


    port = 587  
    smtp_server = "smtp.gmail.com"
    sender_email = "bigoinvestment291@gmail.com"    #use your email1
    receiver_email = "prabinbohara10@gmail.com"    #use your email2
    password = input("Enter your password!")

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)