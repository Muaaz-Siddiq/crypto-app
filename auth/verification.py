from flask import Blueprint, request, jsonify
from config import *
from utils.mailSender import *
from urllib.parse import urlparse
import random , string
import pymongo
import os
from dotenv import load_dotenv
load_dotenv(find_dotenv())



verification = Blueprint("verification", __name__)

@verification.route('/email', methods=['GET','POST'])
def email_verification():
    try:
        if request.method == 'POST':
            email = request.get_json()['email']
            random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=30))

            collection.find_one_and_update({"email":email},{ '$set': { "email_code" : random_str} })
            
            parsed_uri = urlparse(request.base_url)
            result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
            mail_link = f'{result}email/verified?q=' + random_str
            message = f"Subject:Email Verification\n\nYour email verification link: {mail_link}"

            messages = sendMail(email=email, message=message)

            return jsonify(messages)
    
    except Exception as e:
        print(e)
        return jsonify({"message":"Something Went Wrong", "status code":500})


