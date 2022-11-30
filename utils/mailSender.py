from config import *
import smtplib, ssl
import os
from dotenv import load_dotenv
load_dotenv(find_dotenv())


def sendMail(**kwargs):

    try:
        print(kwargs['email'], 'and', kwargs['message'])
        
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        # server.starttls()
            smtp.login('testdeveloper1599@gmail.com', 'test@test1234567')
            smtp.sendmail('testdeveloper1599@gmail.com', kwargs['email'], kwargs['message'])
            return {"message":"mail send successfully", "status code": 200} 

    except Exception as e:
        print(e)
        return {"message":"Something Went Wrong", "status code": 500}