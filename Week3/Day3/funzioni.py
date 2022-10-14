
"""

def insert_author(name,song):
    sql = "INSERT INTO autore (nome, titolocanzone) VALUES (%s, %s)"
    name = str(name)
    song = str(song)
    val = (name, song)
    cursor.execute(sql, val)


def somma(a,b):
    return a+b


def somma_differenza(a,b):
    if a >0 and b>0:
        return a+b
    else:
        return a-b
"""



def print_puttana_lista(l):
    lunghezza_lista = leggi(l)
    for i in range(0,leggi(l)):
        print(l[i])


def leggi(l):
    lunghezza = 0
    for i in l:
        lunghezza += 1
    return lunghezza

lista = [1,2,3,4,5,6]

n = leggi(lista)
print(n)

print(lista)
print_puttana_lista(lista)
