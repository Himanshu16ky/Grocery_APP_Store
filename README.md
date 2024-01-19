# Grocery Store v2

A Website where user can buy Grocery items, Manager and Admin run the store as per role, Additional features include : Backend jobs like export, alert and reporting jobs.

# Features :

- User authentication : Signup and Login (Token Based Authentication - JWT).

- User Dashbord: Add items to cart,Dynamic pricing and item counting, Out-of-Stock feature.

- Search Funcationality: can filter and search items on the basis of price and name.

- Cart: Add and remove items, Out-of-Stock functionality, Purchase Items

- Manager Dashbord: Add, remove and edit Categories with the permission of Admin.
Add, remove and edit Items with a conformation.

- Admin: Approve or deny the the requests of Manager , Add new Manager

- Handling  Images: Add images to a item with the backen server live time

- Performance and Caching: added caching & cache expiry where required to increase the API performance.

- Scheduled Jobs : Send monthly progress report using mail.

- Daily Reminder Jobs : Receive daily reminders to post.

- User Triggered Async Job: Export blog details as CSV


# Technologies Used :

- Flask: backend API is developed using Flask, a lightweight and flexible web framework for Python.

- VueJS: frontend UI is built using VueJS CLI, a popular JavaScript framework for building user interfaces.

- Jinja2 templates: used for rendering HTML templates and sending emails.

- Bootstrap: used for styling and UI components to create an attractive and responsive user interface.

- SQLite and SQLAlchemy: SQLite database is used for data storage.

- Flask-Restful: used to develop the RESTful API for the app

- Flask-SQLAlchemy: used to access and modify the app's SQLite database.

- Flask-Celery: used for asynchronous background jobs at the backend.

- Flask-Caching: used for caching API outputs and increasing performance.

- Redis: used as an in-memory database for the API cache and as a message broker for celery.

# Instructions to run the application.
1. Start redis-server and redis-cli in windows.

2. Navigate to the root -> backend folder of the application.
	open three seprate terminal in backend dir:
	-> execute "python main.py" in terminal
	-> celery -A main.celery worker --pool=solo -l info
	-> celery -A main.celery beat --max-interval 600 -l info

3. Navigate to the root -> frontend folder of the application.
	open terminal in frontend dir:
	-> execute "npm run serve" in terminal


# Support my work
Do ⭐ the repository, if it inspired you, gave you ideas for your own project or helped you in any way !!!