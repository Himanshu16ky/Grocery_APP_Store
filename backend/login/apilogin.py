from email.message import EmailMessage
from functools import wraps
import json
import time
from flask import flash, jsonify, make_response, redirect, render_template, request, session, url_for
from flask_restful import Resource, reqparse
from itsdangerous import Serializer
import jwt
from datetime import timedelta
from datetime import datetime
import smtplib

import requests
from db.database import Users,db,Requests


from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime,timedelta
from functools import wraps
from flask import jsonify, make_response, redirect, render_template, request, session, url_for,current_app
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, set_access_cookies
from flask_login import login_user
from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash
from itsdangerous import URLSafeTimedSerializer
from flask_login import LoginManager


app = current_app
security_code = "safe"
app.config['SECRET_KEY'] = "secure_as_hell"
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True,
                    help='Username is required !!')
parser.add_argument('password', type=str, required=True,
                    help='Password is required !!')
dic={}
flag= False


login_manager = LoginManager(app)
confirmation_status = {}
@login_manager.user_loader
def load_user(user_id):
    # Implement this function to load a user by their ID
    # Example: return User.query.get(int(user_id))
    return None  # Replace with your actual user loading logic

@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email = serializer.loads(token, salt='email-confirm', max_age=3600)
        print(f'Email confirmed: {email}')
        flash('Verified.\nGoto Login Page', 'success')
        flag = True
        dic["flag"] = True
        confirmation_status[email] = True
        print(flag)

        return render_template('confirm_mail.html',message="Your Email has been Confirmed.\n You may proceed to Registeration")
    
    except Exception as e:
        print(e)
        return render_template('confirm_mail.html',message="The confirmation link is invalid or has expired.")


class apilogin(Resource):
    def ff(self):
        session['aaa'] = 'aaaouu'
    
    def post(self):
        print("logging in ..........")
        args = parser.parse_args()
        username = args.get('username')
        password = args.get('password')
        print(username,password)
        user = Users.query.filter_by(username=username).first()
        print(user,"......................")
        if user.username == username and user.password == password:
            refresh_token = create_refresh_token(identity=username, expires_delta=timedelta(hours=30))
            access_token = create_access_token(identity=username, expires_delta=timedelta(hours=10))

            role = user.role
            # token = jwt.encode({'user': username, 'exp': datetime.utcnow(
            #         ) + timedelta(seconds=30)}, security_code, algorithm='HS256')
            print("insideif......................")
            print("before returning")

            self.ff()
            print(session.get('aaa'))
            user.time_stamp = datetime.now()
            db.session.commit()

            return jsonify({'status': 'successful',
                            'message': 'Successfully logged in !!',
                            "refresh_token":refresh_token,
                             'access_token': access_token ,
                            "username": username,
                            "role" : role
                            })
        else:
            print("else..............................")
            return jsonify({'status': 'unsuccessful'})

class apiregister(Resource):   
    def post(self):
        print("registering..........")
        res  = request.get_json()
        print(res)
        args = parser.parse_args()
        print(res["username"],res["password"],res["email"],res["role"])

        isuser = Users.query.filter_by(username=res["username"]).first()
        isemail = Users.query.filter_by(email=res["email"]).first()
        username_registering = Requests.query.filter_by(name=res["username"]).first()
        email_registering = Requests.query.filter_by(type="joining").all()
        email_found=False
        for e in email_registering:
            if(json.loads(e.details)[0]["email"] == res["email"]):
                email_found = True

        if isuser or username_registering:
            print("username_exist")
            return "username_exist"
        if isemail or email_found:
            print("email_exist")
            return "email_exist"
        if res["role"] == "manager":
            manager_data = { "email":res['email'],
                            "password":res['password'],
                            "role" : res['role']}
            new_manager = Requests(name = res["username"], type = "joining",details = json.dumps([manager_data]))
            db.session.add(new_manager)
            db.session.commit()
            return "pending"

        new_user = Users(username = res["username"], password = res["password"],email = res["email"],role = res["role"])
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            print(e)
            return "unsuccessful"
        
        return "successful"

    def get(self,email):
        print("verifying email...",email)
        dic["flag"]= False
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('test1subject1fake1@gmail.com', 'lrytxxsdwytdjjdl')
            
            token = serializer.dumps(email, salt='email-confirm')
            confirm_url = url_for('confirm_email', token=token, _external=True)

            em = EmailMessage()
            em['From'] = 'test1subject1fake1@gmail.com'
            em['To'] = email
            em['Subject'] = "Register on SnapShop"
            em.set_content(f"Click the following link to confirm your email: {confirm_url}")

            server.send_message(em)

            print("Email sent successfully.")
            while True:
                # if confirmation_status[email]:
                if dic["flag"]:
                    print(dic["flag"],"when true")
                    return True
                    # return jsonify({"success": True, "message": "Email confirmed successfully"})
                else:
                    time.sleep(1)
                    # print(confirmation_status[email])
            print("email clicked")
            return True
    
        except Exception as e:
            print(e)
            return False

            
        # if user.username == username and user.password == password:
        #     refresh_token = create_refresh_token(identity=username, expires_delta=timedelta(hours=30))
        #     access_token = create_access_token(identity=username, expires_delta=timedelta(hours=10))

        #     role = user.role
        #     # token = jwt.encode({'user': username, 'exp': datetime.utcnow(
        #     #         ) + timedelta(seconds=30)}, security_code, algorithm='HS256')
        #     print("insideif......................")
        #     print("before returning")

        #     self.ff()
        #     print(session.get('aaa'))

        #     return jsonify({'status': 'successful',
        #                     'message': 'Successfully logged in !!',
        #                     "refresh_token":refresh_token,
        #                      'access_token': access_token ,
        #                     "username": username,
        #                     "role" : role
                            # })
        # else:
        #     print("else..............................")
        #     return jsonify({'status': 'unsuccessful'})