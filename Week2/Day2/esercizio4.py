"""
Esercizio 4: Scrivi un programma chiede in input all'utente una misura in metri e la converte in miglia, piedi e pollici

"""

metri = 1
miglia = metri * 0.00062137
piedi = metri * 3.2808
pollici = metri * 39.370

metri = int(input("Inserisci la misura in metri che vuoi convertire: "))
print("La conversione di", metri, "è ", miglia, " miglia")
print("La conversione di", metri, "è ", piedi, " piedi")
print("La conversione di", metri, "è ", pollici, " pollici")
