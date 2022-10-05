"""
Esercizio 1: scrivi un programma che trasforma in maiuscolo tutte le consonanti di una stringa in input da tastiera
"""

stringa = 'Totti Blasi, Ilary infuriata perché il Capitano non ha salvato le apparenze con Noemi'

#trasforma in lettere maiuscole
stringa = stringa.upper()

#trasforma le sole vocali in minuscolo
stringa = stringa.replace('A', 'a')
stringa = stringa.replace('E', 'e')
stringa = stringa.replace('I', 'i')
stringa = stringa.replace('O', 'o')
stringa = stringa.replace('U', 'u')

#trasformo la stringa in una lista
lista_parole = list(stringa)

#faccio split delle parole usa lo spazio come separatore
frase_split = stringa.split(' ')

#crea una lista di vocali 
vocali = ['a', 'e', 'i', 'o', 'u']

#crera delle liste vuote una per ogni lettera dove inseriro tutte le parole che contengono quella vocale
parola_con_a = []
parola_con_e = []
parola_con_i = []
parola_con_o = []
parola_con_u = []

dizionario = {
    'a': [],
    'e': [],
    'i': [],
    'o': [],
    'u': []
}

#facciamo un ciclo per ogni vocale in frase_split 
for i in range(0, len(frase_split)):
    if 'a' in frase_split[i]:
        parola_con_a.append(frase_split[i])
#aggiungo le parole che hanno la a alla chiave 'a' nel dizionario
dizionario["a"] = tuple(parola_con_a)

for i in range(0, len(frase_split)):
    if 'e' in frase_split[i]:
        parola_con_e.append(frase_split[i])
dizionario["e"] = tuple(parola_con_e)

for i in range(0, len(frase_split)):
    if 'i' in frase_split[i]:
        parola_con_i.append(frase_split[i])
dizionario["i"] = tuple(parola_con_i)

for i in range(0, len(frase_split)):
    if 'o' in frase_split[i]:
        parola_con_o.append(frase_split[i])
dizionario["o"] = tuple(parola_con_o)

for i in range(0, len(frase_split)):
    if 'u' in frase_split[i]:
        parola_con_u.append(frase_split[i])
dizionario["u"] = tuple(parola_con_u)

print(dizionario)
