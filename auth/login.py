from flask import Blueprint, request, jsonify
from config import *
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from models.loginModel import *
from utils.pydanticError import *
from flask_pydantic import validate

login = Blueprint("login", __name__)


@login.route('/', methods=['GET','POST'])
@custom_error
@validate(body=loginModel)
def login_view():
    try:
        if request.method == 'POST':
            email = request.get_json()['email']
        password = request.get_json()['password']
        user = collection.find_one({'email':email})
        if user and check_password_hash(user['password'], password):
            # pass_check = check_password_hash(user['password'], password)
            # if pass_check:
            refresh_token = create_refresh_token(identity=user['email'])
            access_token = create_access_token(identity=user['email'])

            return jsonify({
                'user':{
                    "id": json_util.dumps(user["_id"]),
                    'fullname':user['fullname'],
                    'email':user['email'],
                    'access':access_token,
                    'refresh':refresh_token
                }
            })
        else:
            return jsonify({"message":'Wrong Credentials'}), 401

    except Exception as e:
        print(e)
        return jsonify({"message":"Something Went Wrong"}), 500