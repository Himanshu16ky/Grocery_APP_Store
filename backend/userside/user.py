# from flask_caching import cache
import json
from flask import jsonify, make_response, redirect, render_template, request, session, url_for
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse
from login.role_required import role_required
from db.database import db , Shop , Category , Users , Userdata
from datetime import datetime
shop_data = {}
products = Shop.query.all()
categories = Category.query.all()

import time

# Record the start time

# Your program logic goes here
# For example, a simple delay

# Record the end time

# Calculate the runtime

from flask_caching import Cache
from flask import current_app as app
cache = Cache(app)

item_list = []
avg = []
# def role_required(role):
#     user = Users.query.filter_by(username=get_jwt_identity()).first()
#     if user.role == role:
#         return True
#     else:
#         return False

sold_data = {}

class userside(Resource):
    @jwt_required()
    @role_required('user')
    def post(self,name):
        print("=============================================")
        print("in user post")
        product = request.get_json()
        print(product)

        cart_item = {
                'item_id': product["item"]["item_id"],
                'product_name': product["item"]["item"],
                'item_count': product["item"]["quantity"],
                'price': product["item"]["price"],
                "exp" : product["item"]["expiry"],
                "pack_size" : product["item"]["pack_size"],
                "stock" : product["item"]["stock"]
            }
        # print(item_list)
        try:
            userdata = Userdata.query.filter_by(username = name).first()
            # print(userdata.cart)
            if userdata.cart == None or userdata.cart == "":
                print("...........")
                userdata.cart = json.dumps([cart_item])
                db.session.commit()
                return "successful"
            else:
                print("else..............")
                old_cart = json.loads(userdata.cart)
                found = False
                for e in old_cart:
                    print(e["item_id"] , product["item"]["item_id"])
                    if e["product_name"] == product["item"]["item"] or e["item_id"] == product["item"]["item_id"]:
                        if product["item"]["quantity"] == 0:
                            old_cart.remove(e)
                            userdata.cart = json.dumps(old_cart)
                            found = True
                            break

                        e["item_count"] = product["item"]["quantity"]
                        e["price"] = product["item"]["price"]
                        e["exp"] = product["item"]["expiry"]
                        e["pack_size"] = product["item"]["pack_size"]
                        e["stock"] = product["item"]["stock"]
                        userdata.cart = json.dumps(old_cart)
                        found = True
                        break
                if found == False:
                    old_cart.append(cart_item)
                    userdata.cart = json.dumps(old_cart)
            db.session.commit()
                        # userdata.cart = json.dumps([cart_item])
                
        except Exception as e:
            print("list not made ::: error ",e)
        # try:
        #     item_details = request.get_json()
        #     # print(name,item_details)
            
        #     item_list += item_details["item"]["item"]
        #     print(item_list)
        #     userdata = Userdata.query.filter_by(username = name).first()
        #     userdata.cart = str(item_list)
        #     # new_item = Userdata(username = name, cart = str(item_list))
        #     # db.session.add(new_item)
        #     db.session.commit()
        #     print(userdata.username,userdata.cart)
        # except Exception as e:
        #     print("erorrrrrrrr",e)
        #     # return e,500
        print("=============================================")
        return "successful"
    
    @jwt_required()
    @role_required('user')
    # @cache.cached(timeout=300, key_prefix='user_data')
    # @cache.cached(timeout=300, key_prefix='data_resource')
    def get(self,name):

        print("in user get<<<<<<<<<<<<<<<<<<,")
        shop_data = {}
        products = Shop.query.all()
        categories = Category.query.all()
        # for e.category in categories:
        #         shop_data[e.category] = []
        # print(shop_data)
        user_cart = Userdata.query.filter_by(username = name).first()

        print(user_cart)
        if user_cart == None:
            new = Userdata(username = name,cart = "[]",purchases = "[]")
            db.session.add(new)
            db.session.commit()

            # user_cart = ""
        print(name)
        user_cart = Userdata.query.filter_by(username = name).first()
        user_cart = json.loads(user_cart.cart)
        for e in products:
            if e.category_name not in shop_data:
                shop_data[e.category_name] = [{
                    "item_id" : e.id,
                    "item" : e.item,
                    "price" : e.price,
                    "stock" : e.stock,
                    "unit" : e.unit,
                    "image" : e.image,
                    "expiry" : e.expiry,
                    "item_count" : 0,
                    "pack_size" : e.pack_size,
                }]
            else:
                shop_data[e.category_name].append({
                    "item_id" : e.id,
                    "item" : e.item,
                    "price" : e.price,
                    "stock" : e.stock,
                    "unit" : e.unit,
                    "image" : e.image,
                    "expiry" : e.expiry,
                    "item_count" : 0,
                    "pack_size" : e.pack_size,
                })
        # print(shop_data)
        print("returned")

        return [shop_data,user_cart]
    
    @jwt_required()
    @role_required('user')
    def delete(self,name,item):
        print("++++++++++++++++++++++++++++++++++++++++++++++")
        s = ""
        print("user cart delete invoked")
        print(name,item)
        try :
            data = Userdata.query.filter_by(username = name).first()
            print(data)
            srtin = data.cart
            
            lst = srtin.split(",")
            lst.remove(item)
            print(lst)
            for e in lst:
                s += e+","
            new_data = s[:-1]
            print(new_data)
        except Exception as e:
            print("error in delete ::: ",e)

        try:
            print("another try")
            data.cart = new_data
            db.session.commit()
        except Exception as e:
            print("deleteion error in table ::;", e)
        print("++++++++++++++++++++++++++++++++++++++++++++++")
        
class cart(Resource):
    def post(self,name):
        print("in cart post",name)
        remove = False
        data = request.get_json()
        print("the data going to be purchased :",data)
        if data["data"]["item_count"] == 0:
            remove = True
        print(data)
        cart = Userdata.query.filter_by(username = name).first()
        data_list = json.loads(cart.cart)
        count = 0
        for e in data_list:
            if e["item_id"] == data["data"]["item_id"]:
                if remove:
                    data_list.pop(count)
                else:
                    e["item_count"] = data["data"]["item_count"]
                cart.cart = json.dumps(data_list)
                break
            count+=1
        db.session.commit()
        print(cart.cart)
        return "successful"
    
    def get(self,name):
        print("in cart get ", name)
        userdata = Userdata.query.filter_by(username = name).first()
        if userdata.cart == "[]":
            print("empty")
            return "empty"
        # print(userdata.cart)
        data_list = json.loads(userdata.cart)
        print("first load cart",data_list)
        print()
        print()
        for e in data_list:
            # if e["product_name"] == data["data"]["product_name"]:
            shop_data = Shop.query.filter_by(id = e["item_id"]).first()
            print(type(shop_data.item))
            print(shop_data.id)
            if shop_data == "" or shop_data == None:
                # cart me se ye wala item hta de
                # price bhi minus krrna h 
                print("breaking")
                break
            e["product_name"] = shop_data.item
            e["price"] = shop_data.price
            e["exp"] = shop_data.expiry
            e["pack_size"] = shop_data.pack_size
            e["stock"] = shop_data.stock
            # e["product_name"] = shop_data.unit,
        
        userdata.cart = json.dumps(data_list)
        print("to dump cart",data_list)
        print()
        print()
        db.session.commit()   
        data = json.loads(userdata.cart)
        print("to load cart",data)
        return data


class purchase(Resource):
    def post(self,name):
        count = 0
        data = request.get_json()
        # print(data)
        print(data["purchasing"])
        for e in data["purchasing"]:
            print(e["product_name"],e["item_count"])
            # try:
            shop = Shop.query.filter_by(item= e["product_name"]).first()
            
            if shop.stock >= int(e["item_count"]):
                shop.stock = shop.stock - int(e["item_count"])
                if shop.stock_sold == None: 
                    shop.stock_sold = 0
                    db.session.commit()
                shop.stock_sold =int(shop.stock_sold) + 1
                userdata = Userdata.query.filter_by(username = name).first()
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y,%H:%M:%S")
                dic = {}
                dic["date"] = dt_string
                dic["data"] = data["purchasing"]
                try:
                    history = json.loads(userdata.purchases)
                except:
                    history = []
                cart = json.loads(userdata.cart)
                # for i in cart:
                #     product = Shop.query.filter(item = i["product_name"])
                #     if(product in sold_data.keys()):
                #         sold_data[product.item] += i["item_count"]
                #     else:
                #         sold_data[product.item] = 1
                #     product.stock -= product.pack_size * i["item_count"]
                #     datime = datetime.now()
                #     i['time'] = datime.strftime("%d %B %Y %H:%M%S")
                print("typeeeeee",type(history))
                print(history)
                history.append(dic)
                print("new historyyyyyyyyyy",history)
                userdata.cart = "[]"
                userdata.purchases = json.dumps(history)
            # cart_list = json.loads(userdata.cart)
            # for c in cart_list:
            #     count += 1
            #     if c["product_name"] == e["product_name"]:
            #         cart_list.remove(c)
            # userdata.cart = json.dumps(cart_list)
                
            else:
                return "out_of_stock"
        # except Exception as e:
            # print("error::::::",e)
            # return e
                    
        # print(purchasing[0])
        # for e in purchasing:
        #     print(purchasing[e])
        #     print()
        #     for f in purchasing[e]:
        #         print([f])

        db.session.commit()
        # now = datetime.now()
        # dt_string = now.strftime("%d/%m/%Y,%H:%M:%S")
        # dic = {}
        # dic["date"] = dt_string
        # dic["data"] = data["purchasing"]
        # history.append(dic)
        print("purchasing complete")
        return "successful"