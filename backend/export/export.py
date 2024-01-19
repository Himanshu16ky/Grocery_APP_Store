from flask import request, send_file
from flask_restful import Resource,reqparse
from flask_jwt_extended import jwt_required

from flask import current_app as app
from app.tasks import *
from userside.img_download import get_img

# -------------- 
parser = reqparse.RequestParser()
class ExportAPI(Resource):
    # @jwt_required()
    def get(self):
        with app.app_context():
            print("starting csv export")
            task = export_csv.delay()

            result = task.wait()
            print(result)
            # print(task)

            csv_path = result['csv_path']
            response = send_file(csv_path, as_attachment=True)

            return response
        
class getting_img(Resource):
    # @jwt_required()
    def post(self):
        # args = parser.parse_args()
        args = request.get_json()
        print(args,"args....................")
        name = args.get('name')
        print(name)
        
        with app.app_context():
            print("collecting")
            # get_img.get()
            gett_img.delay(name)
            print("Image collected")