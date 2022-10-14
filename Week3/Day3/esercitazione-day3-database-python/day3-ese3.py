import mysql.connector



def connection(user,password,host,db):
    """
    :param user:
    :param password:
    :param host:
    :param db:
    :return:
    """
    conn = mysql.connector.connect(user,password,host,db)
    return conn

conn = connection()
cursor = conn.cursor()

