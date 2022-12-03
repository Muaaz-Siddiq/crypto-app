from config import *
import smtplib, ssl
import os
from dotenv import load_dotenv
load_dotenv(find_dotenv())


def sendMail(**kwargs):

    try:
        print(kwargs['email'], 'and', kwargs['message'])
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()    
        server.login(os.getenv('SENDER_MAIL'), os.getenv('SENDER_PASSWORD'))
        server.sendmail(os.getenv('SENDER_MAIL'), kwargs['email'], kwargs['message'])
        
        return {"message":"mail send successfully", "status code": 200} 



    except Exception as e:
        print(e)
        return {"message":"Something Went Wrong", "status code": 500}