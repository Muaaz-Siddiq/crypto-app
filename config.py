from flask import Flask
from flask_pymongo import pymongo
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from datetime import timedelta
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# ==================== Initializing App ======================

app = Flask(__name__)

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30) # increasing time duration of tokens
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

jwt = JWTManager(app)



# ==================== DB Connection ====================
try:
    client = pymongo.MongoClient(os.getenv('DB_CONNECTION'))
    db = client['crypto-db']
    collection = db['crypto-collection']
    print('DB Connection success')

except Exception as e:
    print('Database Connection Exception:',e)