
import mysql.connector

conn = mysql.connector.connect(user = 'root',
                               password ='giuschil91',
                               host='localhost',
                               database='amazon')

cursor = conn.cursor()


#voglio inserire un prodotto in database amazon nella tabella prodotti_amazon che ha tre colonne

def insert_product(id,product_name,product_description):
    id = str(id)
    product_name = str(product_name)
    product_description = str(product_description)
    val = (id,product_name,product_description)
    sql = "INSERT INTO prodotti_amazon (id,Nome_prodotto,descrizione_prodotto) VALUES (%s, %s, %s)"
    cursor.execute(sql, val)

sql = insert_product('12345','supersantos','pallone arancione')


try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()


"""
def select_table(name_column,table_name)
    name_column = str(name_column)
    query = 'select' + name_column  + ' from ' + table_name + ';'
    return query

sql = select_table(cognome,ordini)

"""
"""
table = []
nome_prodotto=[]

for i in range(0,10):
    delete_product(table,nome_prodotto)
    
"""
def delete_author(name,song):
    sql = "DELETE FROM autore WHERE nome = %s and TitoloCanzone = %s"
    name = str(name)
    song = str(song)
    val = (name, song)
    cursor.execute(sql, val)


def delete_product(table,prodotto):
    #table = str(table)
    #nome_prodotto = str(nome_prodotto)
    #sql = "DELETE FROM %s WHERE Nome_prodotto = %s"
    sql = "Delete from " + str(table) + " where " + "Nome_prodotto = " + str(prodotto) + ";"
    print(sql)
    cursor.execute(sql)


#sql_delete = delete_product('prodotti_amazon','supersantos')


def select_table(name_column1,name_column2,table_name):
    name_column = str(name_column1)
    name_column2 = str(name_column2)
    query = 'select ' + name_column1 +' , '+name_column2 + ' from ' + table_name + ';'
    return query



sql = select_table('id','nome_prodotto','prodotti_amazon')

try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()

#result = cursor.fetchall();

def print_table(query):
    for i,j in result:
        print(i,j)

cursor.execute(sql)
result = cursor.fetchall();

print_table(result)
