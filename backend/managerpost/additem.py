from flask import jsonify, make_response, redirect, render_template, request, session, url_for
from flask_restful import Resource, reqparse
from db.database import db
from db.database import Shop
from db.database import Category

security_code = "safe"
# cors = CORS(app,supports_credentials=True)  

parser = reqparse.RequestParser()
parser.add_argument('new_category', type=str, required=True,
                    help='Username is required !!')
parser.add_argument('id_', type=str, required=True,
                    help='Username is required !!')


class additem(Resource):
    def post(self,name):
        print("item post..........")
        # if name:
        # new_category = request.data.decode('utf-8')
        data = request.get_json()  
        print("data : ",data)
        # itemname = 
        # expdate = 
        # unit =
        # price = 
        # stock =
        category_table = Category.query.filter_by(category = data["category"]).first()
        # print(category_table.category_id,category_table.category)
        table = Shop.query.filter_by(item = data["item"]).first()
        # table = Shop.query.filter_by(categoryid = category_table.category_id).first()
        
        try:
            if table:
                print("item name alreaty present")
                return "duplicate"
        except Exception as e :
            print("ERROR::::::",e)

        try:
            addcolumn = Shop(item = data["item"],categoryid = category_table.category_id,category_name = category_table.category,price = data["price"],stock = data["stock"],unit= data["unit"],expiry= data["expiry"],pack_size = data["pack_size"])
            db.session.add(addcolumn)
            db.session.commit()
            result = Shop.query.filter_by(categoryid = category_table.category_id).all()
            print(result)
            shop_data = []
            for shop in result:
                shop_data.append({
                'categoryid': shop.categoryid,
                'item': shop.item,
                'price': shop.price,
                'stock': shop.stock,
                'unit': shop.unit,
                'image': shop.image,
                'expiry': shop.expiry,
                'item': shop.item,
                'size':shop.pack_size,
            })
            print(shop_data)
            return shop_data
        except Exception as e:
            print("ERROR : ",e)
        return "unseccessful"
        # return "successful"
        # table = Category.query.filter_by(category=new_category["data"]).first()

    def get(self,name):
        print(name)
        category_table = Category.query.filter_by(category = name).first()
        print(category_table)
        items = Shop.query.filter_by(categoryid = category_table.category_id).all()
        shop_data = []
        for shop in items:
            shop_data.append({
            'categoryid': shop.categoryid,
            'category_name': shop.category_name,
            'item': shop.item,
            'price': shop.price,
            'stock': shop.stock,
            'unit': shop.unit,
            'image': shop.image,
            'expiry': shop.expiry,
            'item': shop.item,
            'size':shop.pack_size,
        })
        return jsonify(shop_data)
    
    def put(self,name):
        print("in put=--=-=-=-=-=-=-=")
        # args = parser.parse_args()
        # id = args.get('data')
        data =  request.get_json()
        print(data)
        oldname = data["editItemName"]
        newname = data["item"]
        table = Shop.query.filter_by(item = oldname).first()
        table2 = Shop.query.filter_by(item = newname).first()
        print(oldname,newname)
        if table != table2 and table2:


        # print(data["oldname"],data["newname"])
        # id = request.get_json()
        # print(id)

        # if data["editItemName"] == data["item"]:

            print("duplicate")
            return "duplicate"
        print(table)
        
        # table = Shop.query.filter_by(item = data["item"],
        #         expiry = data["expiry"],price = data["price"],
        #         stock = data["stock"],unit = data["unit"],).first()
        
        try:
            # for e in table:
            #     print(e)
            table.item = data["item"]
            table.expiry = data["expiry"]
            table.price = data["price"]
            table.stock = data["stock"]
            table.pack_size = data["pack_size"]
            table.unit = data["unit"]
            db.session.commit()
        except Exception as e:
            print(e)
            response_data = {"alert": "Category Name already exist !!"}
            return jsonify(response_data)
        return "successful"

class delet(Resource):
    def delete(self,itemname):
        print(itemname)
        to_delete = Shop.query.filter_by(item = itemname).first()
        print(to_delete)
        db.session.delete(to_delete)
        db.session.commit()
        return "successful"
