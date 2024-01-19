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

def sendDailyReminderMail():
    users = Users.query.filter_by(role = 'user').all()
    print(users.time_stamp)

    for user in users:
        if datetime.now() - datetime.strptime(user.time_stamp, "%Y-%m-%d %H:%M:%S.%f") > timedelta(hours=24):
            # send_email.delay(user.email)
            print("email sent to ", user.username)

    return 'Daily Reminder sent successfully via MAIL !!'
sendDailyReminderMail()

# def send_email(email):
#     print("Sending email...")
    
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login('726ryadav@gmail.com', 'bjtzpedlxrimemlt')

#     em = EmailMessage()
#     em['From'] = '726ryadav@gmail.com'
#     em['To'] = email
#     em['Subject'] = "🌟 Discover Exciting Offers at Urahara's Shop - Limited Time Only! 🌟"
#     em.set_content(f"We hope this message finds you well. We are always looking for ways to enhance your shopping experience and provide you with the best offers on quality products.We're excited to invite you to explore our online grocery store, where you can discover a world of convenience and savings.\n\nAs a token of our appreciation, we're offering a special 17% discount on your first online order. Use code: [WELCOME20] at checkout.\nThank you for being a valued customer. We look forward to serving you online and providing you with a delightful shopping experience.\n\nBest regards,\nSoul Society")

#     server.send_message(em)
    
#     print("Sent")