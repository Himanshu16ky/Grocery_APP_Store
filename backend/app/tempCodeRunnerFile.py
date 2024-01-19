def sendDailyReminderMail():
    users = Users.query.filter_by(role = 'user').all()
    print(users.time_stamp)

    for user in users:
        if not user.time_stamp or datetime.strptime(user.time_stamp , "%Y-%m-%d %H:%M:%S.%f") < datetime.now() - timedelta(days=1):
            send_email.delay(user.email)

    return 'Daily Reminder sent successfully via MAIL !!'
sendDailyReminderMail()