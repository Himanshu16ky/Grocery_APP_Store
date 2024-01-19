import csv
from datetime import datetime, timedelta
import json
import smtplib
import ssl
from email.message import EmailMessage

from flask import render_template,current_app
from db.database import Users,db,Shop,Userdata

from app.workers import celery
from celery.schedules import crontab
import os
# from userside.user import sold_data
# from api.dashboard.checkout import dic

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(
        crontab(minute=00, hour=19),
        sendDailyReminderMail.s(),
        name = 'Daily reminder everyday @7PM via mail.',
    )

    sender.add_periodic_task(
        crontab(minute=1, hour=11),
        # crontab(day_of_month=1, month_of_year='*'),
        sendMonthlyMail.s(),
        name = 'Monthly Activity Report @1st of every month via mail.',
    )



# 1. DAILY reminder TASKS [Daily Reminder Jobs]
# -----------------------


@celery.task
def send_email(email):
    print("Sending email...")
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('test1subject1fake1@gmail.com', 'lrytxxsdwytdjjdl')

    em = EmailMessage()
    em['From'] = 'test1subject1fake1@gmail.com'
    em['To'] = email
    em['Subject'] = "🌟 Discover Exciting Offers at SnapShop - Limited Time Only! 🌟"
    em.set_content(f"We hope this message finds you well. We are always looking for ways to enhance your shopping experience and provide you with the best offers on quality products.We're excited to invite you to explore our online grocery store, where you can discover a world of convenience and savings.\n\nAs a token of our appreciation, we're offering a special 17% discount on your first online order. Use code: [WELCOME20] at checkout.\nThank you for being a valued customer. We look forward to serving you online and providing you with a delightful shopping experience.\n\nBest regards,\nSoul Society")

    server.send_message(em)
    
    print("Sent")


@celery.task
def sendDailyReminderMail():
    users = Users.query.filter_by(role = 'user').all()

    for user in users:
        print(user.time_stamp,"sending mail for daily reminder")

        if datetime.now() - datetime.strptime(user.time_stamp, "%Y-%m-%d %H:%M:%S.%f") > timedelta(hours=24):
            send_email.delay(user.email)
            print(user.username,"haven't come online since past 24 hours")

    return 'Daily Reminder sent successfully via MAIL !!'



# 2. MONTHLY mail - tasks [Scheduled Job - Monthly Activity Report]
# -------------------------

@celery.task
def sendMARMail(name, email):
    user = Userdata.query.filter_by(username=name).first()
    print("username : ",user.username)
    print(user.purchases)
    if(user.purchases != None):
        print("ander")
        orders = json.loads(user.purchases)
        message_html = render_template('monthly_rep.html', orders=orders, has_orders=True)
        
        today = datetime.today().strftime('%B-%Y')
        subject = f'SnapShop: Monthly Activity Report for ({today})'

        # Create the plain text version of the email (optional)
        message_plain = ""

        # Set up the email message
        em = EmailMessage()
        em['From'] = 'test1subject1fake1@gmail.com'
        em['To'] = email
        em['Subject'] = subject
        em.set_content(message_plain)  # Set plain text content
        em.add_alternative(message_html, subtype='html')  # Set HTML content

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('test1subject1fake1@gmail.com', 'lrytxxsdwytdjjdl')
        server.send_message(em)
        server.quit()

        print("yeho")

    # return f'Monthly review email sent to {email}'
    else:
        print("no data to send",user.username)



@celery.task
def sendMonthlyMail():
    users = Users.query.filter_by(role = 'user').all()
    print(users)
    for user in users:
        sendMARMail.delay(user.username, user.email)
    print('Monthly mail has been sent.')
    return 'Monthly mail has been sent.'




# 3. EXPORT tasks [User Triggered Async Job - Export as CSV]
# ----------------

@celery.task
def export_csv():
    with current_app.app_context():

        # 1. Generating Product CSV
        # -----------------------
        print("inside export_csv ...................")
        prod_list = ['id', 'item', 'price', 'category_name', 'stock_left', 'stock_sold']
        products = db.session.query(Shop).all()

        rows = []
        for product in products:
            print(product.id)
            print(product.item)
            print(product.price)
            print(product.category_name)
            # print(product.pack_size)
            # print(product.unit)
            print(product.stock)
            print(product.stock_sold)
            # print(sold_data)
            try:
                # pass
                row = [product.id, product.item, product.price, product.category_name,product.stock,product.stock_sold]
            except Exception as e:
                print("exception accured in tasks at line 154", e)
                #  row = [product.id, product.item, product.price, product.pack_size,product.unit, product.stock, 0]
            rows.append(row)

        now = datetime.now().strftime("%d-%m-%Y_%H%M")
        product_filename = f'profile_{now}.csv'

        csv_path = os.path.join('templates/CSV exports/', product_filename)

        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        print('PRODUCTS FILE SAVED!!')

        with open(csv_path, 'w', newline='') as csvfile:
            print("inside with,,,,,,,,,,,,,,")
            csvwriter = csv.writer(csvfile)

            if csvfile.tell() == 0:
                csvwriter.writerow(prod_list)

            csvwriter.writerows(rows)
            
        return  {'status': 'success', 'message': 'Post & Profile CSVs - Created Successfully !!', 'csv_path': csv_path}
    


from bing_image_downloader import downloader


basedir = os.path.abspath(os.path.dirname(__file__))

basedir = (basedir.replace("\\","/")) 
print(basedir)
basedir = basedir[:-16] + "/him/frontend/public/images"

@celery.task
def gett_img(name):
    print("inside this function that was not there previously called")
    with current_app.app_context():
        print("inside image downloader")
        product = Shop.query.filter_by(item = name).first()
        print(product.item,"mmmmmmmmmmm")
        downloader.download(product.item, limit=1,  output_dir=basedir,adult_filter_off=True, force_replace=False, timeout=30)
        files = os.listdir(basedir + f"/{product.item}")
        product.image = f'images/{product.item}/{files[0]}'
        print("image address aaaaaaaaaaadded",name)
        db.session.commit()