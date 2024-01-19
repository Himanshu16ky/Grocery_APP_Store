from flask_sqlalchemy import SQLAlchemy
# from flask import Flask,url_for,request,jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///' + os.path.join(basedir, 'databse.sqlite3'))
db = SQLAlchemy()
# db.init_app(app)
# app.app_context().push()
# CORS(app)  # Enable CORS for all routes

class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, nullable = False, unique = True, primary_key = True)
    category = db.Column(db.String, unique = True)

class Users(db.Model):
    __tablename__ = 'users'
    userid = db.Column(db.Integer, nullable = False, primary_key = True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String,unique = True,)
    role = db.Column(db.String)
    purchases = db.Column(db.String)
    time_stamp = db.Column(db.String)

class Userdata(db.Model):
    __tablename__ = 'userdata'
    username = db.Column(db.String, unique = True, primary_key = True)
    cart = db.Column(db.String)
    purchases = db.Column(db.String)

class Shop(db.Model):
    __tablename__ = 'shop'
    id = db.Column(db.Integer, nullable = False, unique = True, primary_key = True)
    categoryid = db.Column(db.Integer )
    category_name = db.Column(db.String)
    item = db.Column(db.String)
    price = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    unit = db.Column(db.String)
    image = db.Column(db.String)
    expiry = db.Column(db.String)
    pack_size = db.Column(db.Integer)
    stock_sold = db.Column(db.Integer)

class Requests(db.Model):
    __tablename__ = "requests"
    req_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    details = db.Column(db.String, unique = True)
# @app.route('/')
# def print_shop():
#     print("in the shop")
#     return "Check the console for printed data"


# @app.route('/api/receive_data', methods=['POST'])
# def receive_data():
#     print("inside receive data")
#     data = request.form.get('data') # Get the JSON data from the request
#     # Process the data as needed
#     return jsonify({'message': 'Data received successfully'})


# if __name__ == "__main__":
#     app.run(debug = True)