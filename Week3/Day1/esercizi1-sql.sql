"""n1. Le città con un aeroporto di cui non è noto il numero di pistte;"""
"""n2. I tipi di aereo usati nei voli che partono da Torino"""
"""n3. Le città da cui partono voli diretti a Bologna"""
"""n4. Le città da cui parte e arriva il volo con codice az274"""
"""n5. Il tipo di aereo, il giorno della settimana, l'orario di partenza la cui città di partenza inizia per B e contiene O e la cui città di arrivo 
termina con A e contiene E"""

"""AEROPORTO(Citta, Nazione,NumPiste)
VOLO(IdVolo, GiornoSett,CittaPart,OraPart,CittaArr, OraArr,TipoAereo)
AEREO(TipoAereo, NumPasseggeri,QtaMerci)"""

"""n1. Le città con un aeroporto di cui non è noto il numero di pistte;"""
SELECT DISTINCT Citta,
FROM AEREPORTO
WHERE NumPiste IS NULL;

"""n2. I tipi di aereo usati nei voli che partono da Torino"""

SELECT TipoAereo
FROM VOLO
WHERE CittaPart == 'Torino';

"""n3. Le città da cui partono voli diretti a Bologna"""
"""AEROPORTO(Citta, Nazione,NumPiste)
VOLO(IdVolo, GiornoSett,CittaPart,OraPart,CittaArr, OraArr,TipoAereo)
AEREO(TipoAereo, NumPasseggeri,QtaMerci)"""

SELECT DISTINCT CittaPart as città,
FROM VOLO
WHERE CittaArr = 'Bologna'

"""n4. Le città da cui parte e arriva il volo con codice az274"""
SELECT DISTINCT CittaPart,
FROM VOLO
WHERE IdVolo = 'AZ274'

"""n5. Il tipo di aereo, il giorno della settimana, l'orario di partenza la cui città di partenza inizia per B e contiene O e la cui città di arrivo 
termina con A e contiene E"""

"""AEROPORTO(Citta, Nazione,NumPiste)
VOLO(IdVolo, GiornoSett,CittaPart,OraPart,CittaArr, OraArr,TipoAereo)
AEREO(TipoAereo, NumPasseggeri,QtaMerci)"""

SELECT TipoAereo, GiornoSett, OraPart
FROM AEREO as a, VOLO as v
WHERE a.TipoAereo = v.TipoAereo
WHERE CittaPart LIKE 'B%O%' AND CittaArr LIKE = '%E%A'

SELECT TipoAereo, GiornoSett, OraPart
FROM  VOLO
WHERE CittaPart LIKE 'B%O%' AND CittaArr LIKE = '%E%A'




