from flask import jsonify, make_response, redirect, render_template, request, session, url_for
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse
from db.database import Users, db
from db.database import Category
from db.database import Requests
from db.database import Shop
from login.role_required import role_required


security_code = "safe"
# cors = CORS(app,supports_credentials=True)  

parser = reqparse.RequestParser()
parser.add_argument('new_category', type=str, required=True,
                    help='Username is required !!')
parser.add_argument('id_', type=str, required=True,
                    help='Username is required !!')

# def role_required(role):
#     user = Users.query.filter_by(username=get_jwt_identity()).first()
#     if user.role == role:
#         return True
#     else:
#         return False

class addcat(Resource):
    # @jwt_required()
    # @role_required('manager')
    def post(self):
        print("manager post..........")
        # new_category = request.data.decode('utf-8')
        new_category = request.get_json()  
        table = Category.query.filter_by(category=new_category["data"]).first()
        if table:
            # token = jwt.encode({'user': username, 'exp': datetime.utcnow(
            #         ) + timedelta(seconds=30)}, security_code, algorithm='HS256')
            print("inside manager if......................")
            return "duplicate"
            # return jsonify({'status': 'successful','message': 'Successfully logged in !!', 'token': 'token' , "username": username})
        else:
            print("else..............................")
            # new_req = request()
            try:
                
                new_request = Requests(name = new_category["person"], type = "add category", details = new_category["data"])
                db.session.add(new_request)
                db.session.commit()
            except Exception as e:
                print("error while manageradding category : ",e)
                return "duplicate"
            return "sent"

    # @jwt_required()
    # @role_required('manager')
    def get(self):
        if (role_required('manager')):
            print("outside role required")
            if(role_required('manager')):
                print("in get ||||||||")
                categories = Category.query.all()
                data_list = [{'id': item.category_id, 'name': item.category} for item in categories]
                return jsonify(data_list)
            else:
                print("forbidden")
                return "forbidden"
        else:
            print("forbidden")
            return "forbidden"

    def put(self):
        print("in put=--=-=-=-=-=-=-=")
        # args = parser.parse_args()
        # id = args.get('data')
        data =  request.get_json()
        print(data,"************")
        print(data["oldname"],data["newname"])
        # id = request.get_json()
        # print(id)
        to_category = Category.query.filter_by(category = data["newname"]).first()
        to_category2 = Category.query.filter_by(category = data["newname"]).first()
        if to_category:
            return "duplicate"
        try:
            edit_row = Requests(name = data["person"], type = "edit category",details = data["oldname"]+" -> "+data["newname"])
            db.session.add(edit_row)
            db.session.commit()
        except Exception as e:
            print(e)
            return "duplicate"
        table = Category.query.filter_by(category = data["oldname"]).first()
        
        # try:
        #     # for e in table:
        #     #     print(e)
        #     table.category = data["newname"]
        #     db.session.commit()
        # except Exception as e:
        #     print(e)
        #     response_data = {"alert": "Category Name already exist !!"}
        #     return jsonify(response_data)
        return "sent"
    
    def delete(self,id,manager):
        print(id)
        row = Category.query.filter_by(category_id = id).first()
        print("in delete -=-=-=-=-,,,,=-=-=-=")
        # print(row.category)
        # already_present = Requests.query.filter_by(details = row.category).first()
        # print(already_present)
        # if already_present:
        #     return "duplicate"
        # else:
        try:
            new_request = Requests(name = manager, type = "delete category", details = row.category)
            db.session.add(new_request)
            db.session.commit()
        except Exception as e:
            print(e)
        return "sent"
    
# class dele(Resource):
#     def delete(self,id):
#         print(id)
#         row = Category.query.filter_by(category_id = id).first()
#         print("in delete -=-=-=-=-=-=-=-=")
#         # print(row.category)
#         already_present = Requests.query.filter_by(details = row.category).first()
#         if already_present:
#             return "duplicate"
#         else:
#             new_request = Requests(name = row.category, type = "delete category", details = row.category)
#             db.session.add(new_request)
#             db.session.commit()
#             return "sent"

    # ---use this later---
        # row = Category.query.filter_by(category_id = id).first()
        # rows = Shop.query.filter_by(categoryid = id).all()
        # db.session.delete(row)
        # for e in rows:
        #     db.session.delete(e)
        # db.session.commit()
        
        # return "successful"