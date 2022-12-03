from flask import Blueprint, jsonify, request
from config import *
from models.signupModel import *
from flask_pydantic import validate, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from utils.pydanticError import *


signup = Blueprint('signup', __name__)

@signup.route('/', methods=['GET','POST'])
@custom_error
@validate(body=SignupModel)
def signup_view():
    if request.method == 'POST':
        try:
            # print(request.get_json())
            fullname = request.get_json()['fullname']
            email = request.get_json()['email']
            password = request.get_json()['password']
            phone_no = request.get_json()['phone_no']

            if collection.find_one({'email':email}):
                return jsonify({"message":"User With This Email Already Exsist"}), 400

            else:
                password = generate_password_hash(password)
                collection.insert_one({"fullname":fullname, "email":email, "password":password,
                "phone_no":phone_no, "is_active":"true", "is_verified":"false", "phone_code":"NA",
                "email_code":"NA", "is_subscribe":"false", "sub_valid_till":"0000/00/00 00:00:00"})
                
                return jsonify({"message":'User Created'}), 201
        
        except Exception as e:
            return jsonify({'Error':e, "message": "Internal Server Error"}), 500