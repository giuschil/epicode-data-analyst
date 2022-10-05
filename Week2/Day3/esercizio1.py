"""
Esercizio 1: scrivi un programma che trasforma in maiuscolo tutte le consonanti di una stringa in input da tastiera
"""

stringa = 'Totti Blasi, Ilary infuriata perché il Capitano non ha salvato le apparenze con Noemi'

stringa = stringa.upper()
stringa = stringa.replace('A', 'a')
stringa = stringa.replace('E', 'e')
stringa = stringa.replace('I', 'i')
stringa = stringa.replace('O', 'o')
stringa = stringa.replace('U', 'u')


lista_parole = list(stringa)
frase_split = stringa.split(' ')

vocali = ['a', 'e', 'i', 'o', 'u']

"""
dizionario = {
    'a': ('parola', 'alba'),
    'e': ('giuseppe', 'erba'),
    'i': (),
    'o': (),
    'u': ()
}
"""
"""
vocale_a = 0
vocale_e = 0
vocale_i = 0
vocale_o = 0
vocale_u = 0
"""

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

for i in range(0, len(frase_split)):
    # print(frase_split[i])
    if 'a' in frase_split[i]:
        #vocale_a =vocale_a + 1
        parola_con_a.append(frase_split[i])
dizionario["a"] = tuple(parola_con_a)

for i in range(0, len(frase_split)):
    # print(frase_split[i])
    if 'e' in frase_split[i]:
        #vocale_e = vocale_e + 1
        parola_con_e.append(frase_split[i])
dizionario["e"] = tuple(parola_con_e)

for i in range(0, len(frase_split)):
    # print(frase_split[i])
    if 'i' in frase_split[i]:
        #vocale_i = vocale_i + 1
        parola_con_i.append(frase_split[i])
dizionario["i"] = tuple(parola_con_i)

for i in range(0, len(frase_split)):
    # print(frase_split[i])
    if 'o' in frase_split[i]:
        #vocale_o = vocale_o + 1
        parola_con_o.append(frase_split[i])
dizionario["o"] = tuple(parola_con_o)

for i in range(0, len(frase_split)):
    # print(frase_split[i])
    if 'u' in frase_split[i]:
        #vocale_u = vocale_u + 1
        parola_con_u.append(frase_split[i])
dizionario["u"] = tuple(parola_con_u)

"""
print("lettera a",parola_con_a)
print("lettera e", parola_con_e)
print("lettera i",parola_con_i)
print("lettera o", parola_con_o)
print("lettera u", parola_con_u)
"""
