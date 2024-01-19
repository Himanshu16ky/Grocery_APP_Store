import time
from datetime import datetime, timedelta
from flask import Flask, config, flash, redirect, render_template, request, session, url_for
from flask_caching import Cache
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import matplotlib

import requests
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from functools import wraps
from flask import Flask, request, jsonify, make_response
import jwt
from db.database import db
# from celery_worker import make_celery

# from flask_caching import cache

app = Flask(__name__)
app.config.from_object(config)
app.app_context().push()
app.config['CACHE_TYPE'] = 'RedisCache'  # You can use 'simple', 'memcached', 'redis', etc.
cache = Cache(app)

import app.workers as workers
from app.tasks import *

# CELERY -----------

celery = workers.celery

celery.conf.update(
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    timezone = 'Asia/Calcutta',
    enable_utc = False
)

celery.Task = workers.ContextTask
app.app_context().push()


# celery start
# app.config.update(
#     CELERY_BROKER_URL='redis://localhost:6379/1',
#     CELERY_RESULT_BACKEND='redis://localhost:6379/3'
# )
# celery = make_celery(app)
# @celery.task()
# def add_together(a,b):
#     time.sleep(5)
#     return "a+b"
# celery end


cors = CORS(app,supports_credentials=True)  
# app.use(cors())
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, POST, DELETE, OPTIONS'
    return response

@app.after_request
def after_request(response):
    response = add_cors_headers(response)
    return response
basedir = os.path.abspath(os.path.dirname(__file__))
basedir = (basedir.replace("\\","/")) 
print(basedir)


login_manager = LoginManager()
# login_manager.session_protection = "strong"
# login_manager.login_view = "login"
# login_manager.login_message_category = "info"

login_manager.init_app(app)


app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///' + basedir+ '/db/databse.sqlite3')
# app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///C:/Users/HP/Desktop/him/backend/db/databse.sqlite3')
app.config['SECRET_KEY'] = "zsf"

db.init_app(app)
api = Api(app)
api.init_app(app)

# @app.route("/1")
# def trigger_celery_job():
#     a = add_together.delay(4, 9)
#     return {
#     "Task ID" : a.id,
#     "Task State" : a.state,
#     "Task Result": a.result
#     }
from flask_restful import Resource
from celery import Celery

# class AddTogetherResource(Resource):
#     def __init__(self, celery):
#         self.celery = celery

#     def get(self):
#         result = self.celery.send_task('add_together', (2, 3))
#         return {
#             "Task ID": result.id,
#             "Task State": result.state,
#             "Task Result": result.result
#         }
# api.add_resource(AddTogetherResource, '/api/trigger_celery')



from login.apilogin import apilogin,apiregister
# from api.dashboard.dashboard import dashboard
api.add_resource(apilogin, '/api/login')
api.add_resource(apiregister, '/api/register','/api/register/<email>')

from managerpost.addcat import addcat
api.add_resource(addcat,'/manager/addcat','/manager/addcat/<id>/<manager>')
# api.add_resource(dele,'/manager/addcat/<id>')

from managerpost.additem import additem,delet
api.add_resource(additem,'/manager/<name>')
api.add_resource(delet,'/manager/additem/<itemname>')

# api.add_resource(dashboard, '/dashboard')

from adminside.adminreq import action,remove
api.add_resource(action,"/todo","/todo/<category>")
api.add_resource(remove,"/remove/<req_id>")

from userside.user import userside,cart,purchase
api.add_resource(userside,"/user","/user/<name>") #  ,"/user/<name>/<item>"
api.add_resource(cart,"/user/<name>/cart")
api.add_resource(purchase,"/user/<name>/purchase")

from export.export import ExportAPI,getting_img
api.add_resource(ExportAPI,"/export/report")
api.add_resource(getting_img,"/get_img")

from userside.img_download import get_img
api.add_resource(get_img, '/get_img/<string:itemname>')

# from export.export import ExportAPI, getting_img
# api.add_resource(geting_img,'')
JWTManager(app)

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)


# start redis-server

# run main.py file

# cd backend
# celery -A main.celery worker --pool=solo -l info



# open in another terminal
# cd backend
# celery -A main.celery beat --max-interval 600 -l info


# cd frontend
# npm run serve