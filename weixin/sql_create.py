import pymysql
MYSQL_HOST = 'localhost'

MYSQL_PORT = 3306

MYSQL_USER = 'root'

MYSQL_PASSWORD = '123123'

MYSQL_DATABASE = 'weixin'
#创建数据库
def create_database():
    db = pymysql.connect(host=MYSQL_HOST,user=MYSQL_USER,password=MYSQL_PASSWORD,charset='utf8',port=MYSQL_PORT)
    cursor = db.cursor()
    cursor.execute('CREATE DATABASE weixin DEFAULT CHARACTER SET utf8mb4')
    db.close()

def create_table():
    db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER,database=MYSQL_DATABASE,password=MYSQL_PASSWORD, charset='utf8', port=MYSQL_PORT)
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS articles('
                   'id int(11) NOT NULL,'
                   'title VARCHAR (255) NOT NULL,'
                   ' content text NOT NULL,'
                   'date VARCHAR (255) NOT NULL ,'
                   'wechat VARCHAR (255) NOT NULL ,'
                   'nickname VARCHAR (255) NOT NULL ,'
                   'PRIMARY KEY(id))')
create_table()