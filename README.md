### Overview

This project focuses on creating a platform for students to ask questions and share their knowledge. I got the idea while serving as a CS mentor in my country. Similar to Piazza and Quora, this platform allows students to share their knowledge and leave comments using their own registered accounts.

### Technologies
For the frontend (file static and templates), due to the internet restriction this part was made by Jacqueline, who uses HTML and CSS to do the UI design.

For the backend, I used Flask, python and MySQL to do the backend implementation.

### How to reproduce it locally
To reproduce it locally, first you should clone my repo with 

```git clone https://github.com/Garyouki/QA-platform.git```

Then you should create a ```config.py``` file to include the information of your database and the email configuartion. Here's the example:

```
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'my_database'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# email config for sending email verification
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "XXXXX@qq.com"
MAIL_PASSWORD = "XXXXXX"
MAIL_DEFAULT_SENDER = "XXXXX@qq.com"
# secret key for session
SECRET_KEY = "happyday"
```

After adding the configuration you should run ```python3 app.py``` to run the project locally.


### To do:
Deploy the project so that people can actually use it to solve problems. Due to the travel restriction this part has not been done yet. 



