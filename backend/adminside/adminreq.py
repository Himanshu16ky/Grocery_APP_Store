import json
from flask import jsonify, make_response, redirect, render_template, request, session, url_for
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse
from db.database import db
from db.database import Requests
from db.database import Category
from db.database import Shop
from db.database import Users
from login.role_required import role_required

security_code = "safe"

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

class action(Resource):
    @jwt_required()
    @role_required('admin')
    def put(self,category):
        lis = category.split(" -> ")
        print(lis)
        try:
            to_category = Category.query.filter_by(category = lis[1]).first()
            if to_category:
                print("duplicate")
                req = Requests.query.filter(Requests.details.contains(lis[1])).all()
                for e in req:
                    db.session.delete(e)
                    db.session.commit()
                return "duplicate"
            to_category2 = Category.query.filter_by(category = lis[0]).first()
            to_category2.category = lis[1]
            db.session.commit()

            # db.session.add(to_category)
            req = Requests.query.filter_by(details = category).first()
            db.session.delete(req)
            db.session.commit()
            req2 = Requests.query.filter(Requests.details.contains(lis[1])).all()
            print("here")
            for e in req2:
                db.session.delete(e)

            db.session.commit()
            print(req2)
        except Exception as e:
            print(e)
            return str(e)
        return "successful"

    @jwt_required()
    @role_required('admin')
    def post(self,category):
        print("in real admin post ::::::")
        try:
            to_category = Category(category = category)
            db.session.add(to_category)

            req = Requests.query.filter_by(details = category).first()
            db.session.delete(req)
            db.session.commit()
        except Exception as e:
            print(e)
            return "duplicate"

        return "successful"
    
    @jwt_required()
    @role_required('admin')
    def delete(self,category):
        print(" real admin delete",category)
        try:
            req = Requests.query.filter_by(details = category).first()
            print(req.details)
            db.session.delete(req)
            db.session.commit()

            from_category = Category.query.filter_by(category = category).first()
            category_id = from_category.category_id
            db.session.delete(from_category)
            db.session.commit()

            # from_shop = Shop.query.filter_by(categoryid = category_id).first()
            # or
            from_shop = Shop.query.filter_by(category_name = category).all()
            for c in from_shop:
                db.session.delete(c)
            db.session.commit()
        except Exception as e:
            print(e)
            return str(e)
        return "successful"

    @jwt_required()
    @role_required('admin')
    def get(self):
        if(role_required('admin')):
            print("in admin get")
            requests = Requests.query.all()
            print(requests)
            # print(requests.name)
            add_category = []
            delete_category = []
            edit_category = []
            joining_requests = []
            # data_list = [{'name': item.name,
            #               'type': item.type,
            #               'details': item.details, } for item in requests
            #                 if item.type == "add category"]
            for item in requests:
                if item.type == "add category" :
                    add_category.append({
                        "req_id" :item.req_id,
                        'name': item.name,
                        'type': item.type,
                        'details': item.details})
                if item.type == "delete category" :
                    delete_category.append({
                        "req_id" :item.req_id,
                        'name': item.name,
                        'type': item.type,
                        'details': item.details})
                if item.type == "edit category" :
                    edit_category.append({
                        "req_id" :item.req_id,
                        'name': item.name,
                        'type': item.type,
                        'details': item.details})
                if item.type == "joining" :
                    joining_requests.append({
                        "req_id" :item.req_id,
                        'name': item.name,
                        'type': item.type,
                        'details': json.loads(item.details)[0]["email"]
                        })
            data_list = [add_category,delete_category,edit_category,joining_requests]
            for e in data_list:
                print(e)
                print(",.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,")
            return data_list
        
        else:
            print('forbidden')
            return "forbidden"
        
class remove(Resource):
    @jwt_required()
    # @role_required(['admin'])
    def delete(self,req_id):
        print(req_id)
        req_table = Requests.query.filter_by(req_id = req_id).first()
        print(req_table)
        db.session.delete(req_table)
        db.session.commit()
        return "successful"
    
    @jwt_required()
    # @role_required(['admin'])
    def post(self,req_id):
        try:
            from_req = Requests.query.filter_by(req_id = req_id).first()
            details = json.loads(from_req.details)
            print("mkmkmk",(json.loads(from_req.details)))
            print(details[0]["email"])
            user_table = Users(username = from_req.name ,password =details[0]["password"] ,role =details[0]["role"] ,email = details[0]["email"])
            db.session.add(user_table)
            db.session.commit()
            self.delete(req_id)
        except Exception as e:
            print(e)
            return str(e)
        return "successful"