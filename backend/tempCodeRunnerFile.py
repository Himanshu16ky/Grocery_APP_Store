# import json
# import redis 
# r = redis.Redis(host = 'localhost',port = 6379,db = 0)
# # d1 =(r.get("d1"))
# # print(d1)
# r.set("d2",json.dumps({"data":11}))


# import requests
# import json
# response = requests.get("https://emailvalidation.abstractapi.com/v1/?api_key=cbda399921df482489ba31ca68929fdd&email=25102himanshukumar.2020ece@gmail.com")
# print(response.status_code)
# print()
# print()
# json_data = json.loads(response.text)
# print(json_data['deliverability'])

# s = b'{"email":"25102himanshukumar.2020ece@gmail.com","autocorrect":"","deliverability":"DELIVERABLE","quality_score":"0.95","is_valid_format":{"value":true,"text":"TRUE"},"is_free_email":{"value":true,"text":"TRUE"},"is_disposable_email":{"value":false,"text":"FALSE"},"is_role_email":{"value":false,"text":"FALSE"},"is_catchall_email":{"value":false,"text":"FALSE"},"is_mx_found":{"value":true,"text":"TRUE"},"is_smtp_valid":{"value":true,"text":"TRUE"}}'




from datetime import datetime, timedelta
from functools import wraps
import random
import secrets
from flask import abort, flash, jsonify, make_response, redirect, render_template, request, session, url_for, current_app
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, set_access_cookies
from flask_login import login_user
from flask_restful import Resource, reqparse
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer

from app.models import Login, db

import smtplib
import ssl
from email.message import EmailMessage

app = current_app
app.config['SECRET_KEY'] = "secure_as_hell"
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='Username is required !!')
parser.add_argument('password', type=str, required=True, help='Password is required !!')

dic={}

def send_email(email):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('726ryadav@gmail.com', 'bjtzpedlxrimemlt')
        
        token = serializer.dumps(email, salt='email-confirm')
        confirm_url = url_for('confirm_manager_email', token=token, _external=True)

        em = EmailMessage()
        em['From'] = '726ryadav@gmail.com'
        em['To'] = email
        em['Subject'] = "Register on Urahara's Shop"
        em.set_content(f"Click the following link to confirm your email: {confirm_url}")

        server.send_message(em)

        print("Email sent successfully.")
        return True
    
    except Exception as e:
        print(e)
        return False

@app.route('/confirm_manager_email/<token>')
def confirm_manager_email(token):
    try:
        email = serializer.loads(token, salt='email-confirm', max_age=3600)
        print(f'Email confirmed: {email}')
        print(dic.get('password'))
        
        hashed_password = generate_password_hash(dic.get('password'))
            
        new_user = Login(email=dic.get('email'), password = hashed_password, role='user',cart_items="",previous_order="")
        
        db.session.add(new_user)
        db.session.commit()
                
        flash('Verified.\nGoto Login Page', 'success')
        
        return render_template('confirm_mail.html',message="Your Email has been Confirmed.")
    
    except Exception as e:
        print(e)
        return render_template('confirm_mail.html',message="The confirmation link is invalid or has expired.")

class registerapi(Resource):
    def post(self):
        args = parser.parse_args()
        username = args.get('username')
        password = args.get('password')

        dic['password'] = password
        dic['email'] = username

        user = Login.query.filter_by(email=username).first()

        if user is not None:
            return {'status': 'unsuccessful'}
        
        if send_email(username):
            return {'status': 'confirm_link_send'}
        else:
            return {'status': 'no such email'}