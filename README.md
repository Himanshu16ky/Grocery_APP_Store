<h1 align="center" id="title">Grocery Store V2</h1>

<p id="description">A platform for making online purchases for Grocery items like Blinkit, BigBasket, Zepto etc. Here user can add item to his/her personal cart and make purchases for different items collectively like any usual grocery application. There are two more levels one is Manager and Admin with divided actions along with Batch jobs.</p>

<h2>🚀 Demo</h2>

[https://drive.google.com/file/d/17o3\_Up9dK3SnDA1Qhs5U9FD1dYdB5jd1/view?usp=sharing](https://drive.google.com/file/d/17o3_Up9dK3SnDA1Qhs5U9FD1dYdB5jd1/view?usp=sharing)

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:
* Performance and Caching: added caching & cache expiry where required to increase the API performance.
* Handling Images: Add images to a item with the backend server live time

* What User can do : 
     * Ability to buy multiple products from one or multiple sections.
     * Ability to search multiple products or categories based on their name or price.
     * Ability to see out of stock products that are not available.
     * Ability to see the total amount to be paid for the transaction.
     * Cart button updates Dynamically.
     * Separate Dashboard for cart items.
* What Manager can do :
     * Ability to add, edit and delete Category from the Shop with Admin's permission
     * Ability to add, edit and delete Items from the shop
* What Admin can do :
     * Accepts or deny the request from Manager.
     * Accepts or deny the new Manager joining request.
     * Gets the shop's monthly report.
* Backend Jobs :
     * Scheduled Jobs : Send monthly progress report using mail to the User.
     * Daily Reminder Jobs : Receive daily reminders to the Users.
     * User Triggered Async Job: Export blog details as CSV.



<h2>🛠️ Installation Steps:</h2>

<p>1. Start Redis server and Redis CLI</p>

<p>2. Open the backend directory</p>

```
cd backend
```

<p>3. Open new Terminal to start backend server</p>

```
python main.py
```

<p>4. Open terminal to celery worker.</p>

```
celery -A main.celery worker --pool=solo -l info
```

<p>5. Open Terminal to start celery beat</p>

```
celery -A main.celery beat --max-interval 600 -l info
```

<p>6. Get to the frontend directory</p>

```
cd../frontend
```

<p>7. Open new Terminal to relevant packages</p>

```
npm install
```

<p>8. Open new Terminal to start frontend server</p>

```
npm run serve
```

<p>9. And All Set.</p>

  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Flask
*   VueJS
*   SQLite3
*   SQLAlchemy
*   Redis
*   Celery
*   Jinja
*   Bootstrap
*   CSS

<h2>💖Like my work?</h2>

Star the Repository Your support matters .
