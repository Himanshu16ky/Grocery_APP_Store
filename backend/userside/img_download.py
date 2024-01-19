import os
from bing_image_downloader import downloader
import celery
from flask_restful import Resource
from db.database import Shop,db

basedir = os.path.abspath(os.path.dirname(__file__))

basedir = (basedir.replace("\\","/")) 
basedir = basedir[:-16] + "frontend/public/images"

    
from bing_image_downloader import downloader
    
def download_images(query):
    
    r = downloader.download(query, limit=1,  output_dir=basedir,adult_filter_off=True, force_replace=False, timeout=20)
    print("image downloaded>>>>>>>>>")
    print(r,query)

class get_img(Resource):
    def get():
        products = Shop.query.filter_by().all()

        for product in products:
            print(product.item, product.image)
            if product.image is None or product.image == "":
                download_images(product.item)
                files = os.listdir(basedir + f"/{product.item}")
                product.image = f'images/{product.item}/{files[0]}'
                print("image address adddddded")

        db.session.commit()

        print("Ready to Go..")

