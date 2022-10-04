"""
Esercizio 3: Scrivi un programma che chiede all'utente in input:
i litri di benzina nel serbatoio
L'efficienza espressa in km per litro
Il prezzo della benzina per litro
Quindi visualizza il costo per 100 km e quanta distanza può percorrere l'auto con la benzina nel serbatoio

"""
"""
#consumo = distanza/litri

#litri_serbatoio = int(input("dimmi i litri del serbatio: "))
#prezzo = float(input("dimmi prezzo benzina: "))
#costo_viaggio =litri_serbatoio * prezzo * distanza
#consumo =distanza/litri_serbatoio

#efficienza = int(input("dimmi quanto km fai con un litro di benzina: "))

#print("Il costo del viaggio è: ", costo_viaggio, "€")


#consumo = efficienza * litri_serbatoio

#print("la distanza che può percorrere l'auto con la benzina nel serbatoio è ", consumo)

#costo_viaggio = 100km (distanza(km)) * (1/efficienza(km/litri)) * prezzo (euro/litri)

"""

efficienza = int(input("inserisci efficienza: "))
distanza = 100
consumo = 1/efficienza
prezzo = float(input("inserisci prezzo: "))
costo = distanza * (1/(efficienza))* prezzo


print("il costo del viaggio di 100km è: ", costo, "€")

serbatoio = float(input("inserisci litri serbatoio: "))

km_rimasti = efficienza * prezzo * serbatoio
costo_viaggio = efficienza * serbatoio
print(km_rimasti)
print(costo_viaggio)



