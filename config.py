# The config to connect database
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'my_database'
USERNAME = 'root'
PASSWORD = 'password'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI