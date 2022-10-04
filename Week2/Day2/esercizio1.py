"""
Esercizio 1: Scrivi un programma che trasforma in maiuscolo tutte le
consonanti di una stringa in input da tastiera (le vocali sono a e i o u)
"""

#inserisci la parola in input
parola = input("inserisci una parola: ")

#stringa con tutte le vocali
vocali = 'aeiou'

i = 0
while i < len(parola):
    #se la lettera non è contenuta in vocali allora è una consonante
    if parola[i] not in vocali:
        print(parola[i].upper(),end=' ')
    else:
        print(parola[i].lower(),end=' ')
    i +=1
