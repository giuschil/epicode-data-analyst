import mysql.connector


conn = mysql.connector.connect(user = 'root',
                               password ='giuschil91',
                               host='localhost',
                               database='discografia')

#sql = " INSERT INTO autore (nome,TitoloCanzone) VALUES ('Mogol', 'Il mio canto libero')"
#sql2 = " INSERT INTO canzone (NomeCantante,CodiceReg) VALUES (1, 10001)"


cursor = conn.cursor()
"""
try:
    cursor.execute(sql2)
    conn.commit()
except:
    conn.rollback()
"""


def insert_author(name,song):
    sql = "INSERT INTO autore (nome, titolocanzone) VALUES (%s, %s)"
    name = str(name)
    song = str(song)
    val = (name, song)
    #table = str(table)
    #sql = "INSERT INTO" + table +
    cursor.execute(sql, val)


try:
    insert_author('Marracash', 'Love')
    conn.commit()
except:
    conn.rollback()



def delete_author(name,song):
    sql = "DELETE FROM autore WHERE nome = %s and TitoloCanzone = %s"
    name = str(name)
    song = str(song)
    val = (name, song)
    cursor.execute(sql, val)


#delete_author('Marracash','Io')


lista_autori = ['883','Lucio Battisti','Luche']
lista_canzoni = ['Sei un mito', 'Il mio canto libero','San Lorenzo']


def insert_author(name,song):
    sql = "INSERT INTO autore (nome, titolocanzone) VALUES (%s, %s)"
    name = str(name)
    song = str(song)
    val = (name, song)
    cursor.execute(sql, val)

def insert_list_songs(list_author,list_songs):
    if len(list_author) == len(list_songs):
        for i in range(len(list_author)):
            name = list_author[i]
            song = list_songs[i]
            val = (name, song)
            sql = "INSERT INTO autore (nome, TitoloCanzone) VALUES (%s, %s)"
            cursor.execute(sql, val)


def insert_esecution(codreg,song,year):
    sql = "INSERT INTO autore (CodiceReg, TitoloCanzone,Anno) VALUES (%s, %s,%s)"
    codreg = str(codreg)
    song = str(song)
    year = str(year)
    val = (codreg,song,year)
    cursor.execute(sql, val)


"""
try:
    insert_list_esecution(lista_autori, lista_canzoni)
    conn.commit()
except:
    conn.rollback()
"""


try:
    insert_esecution('10001', 'Il mio canto libero','1978')
    conn.commit()
except:
    conn.rollback()

#sql_show_tables = 'show tables'

sql_show_autore = "select * from autore"
cursor.execute(sql_show_autore)
result = cursor.fetchall();

#print(result)

sql_show_autore = "select * from esecuzione"
cursor.execute(sql_show_autore)
result = cursor.fetchall();


def print_table(query):
    for i,j in result:
        print(i,j)


print_table(result)

conn.close()


query = 'select * from table_name;'

query = 'select' + ' * ' + ' from ' + ' table_name'+';'

def select_table(name_column,table_name)
    name_column = str(name_column)
    query = 'select' + name_column  + ' from ' + table_name + ';'
    return query



def insert_table(name_column,table_name)
    name_column = str(name_column)
    query = 'select' + name_column  + ' from ' + table_name + ';'
    return insert




def select_table(name_column,table_name)
    name_column = str(name_column)
    query = 'select' + name_column  + ' from ' + table_name + ';'
    return query

sql = select_table(cognome,ordini)

try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()

database = 'discografia')
cursor = conn.cursor()
