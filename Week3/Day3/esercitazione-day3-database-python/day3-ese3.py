import mysql.connector

user= 'root'
password = 'giuschil91'
host = 'localhost'
db = 'discografia'


def connect(user,password,host,db):
    """
    :param user:
    :param password:
    :param host:
    :param db:
    :return:
    """
    conn = mysql.connector.connect(user,password,host,db)
    return conn

conn = connect(user,password,host,db)
cursor = conn.cursor()

