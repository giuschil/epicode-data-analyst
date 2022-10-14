"""
DISCO(NroSerie,TitoloAlbum,Anno,Prezzo)
CONTIENE(NroSerieDisco,CodiceReg,NroProg)
ESECUZIONE(CodiceReg,TitoloCanz,Anno)
AUTORE(Nome,TitoloCanzone)
CANTANTE(NomeCantante,CodiceReg)
"""
--n1. I cantautori (persone che hanno cantato e scritto la stessa canzone) il cui nome inizia per 'D' 

SELECT c.NomeCantante as Nome Cantante
FROM cantante AS c INNER JOIN autore AS a ON Nome = NomeCantante
WHERE NomeCantante LIKE 'D%';

--n1. versione diversa

SELECT c.NomeCantante as Nome Cantante
FROM CANTANTE INNER JOIN AUTORE ON Nome = NomeCantante
WHERE NomeCantante LIKE 'D%';

--n2. I titoli dei dischi che contengono canzoni di cui non si conosce l'anno di registrazione

SELECT d.TitoloAlbum AS Titolo 
FROM disco as d INNER JOIN contiene as c as e on d.NroSerie = c.NroSerieDisco 
INNER JOIN c.CodiceReg = e.CodiceReg
WHERE e.Anno IS NULL;


--n2. versione diversa

SELECT d.TitoloAlbum AS Titolo
FROM disco d, contiene c, esecuzione e 
WHERE d.NroSerie = c.NroSerieDisco AND c.CodiceReg = e.CodiceReg
AND e.Anno IS NULL;


"""
DISCO(NroSerie,TitoloAlbum,Anno,Prezzo)
CONTIENE(NroSerieDisco,CodiceReg,NroProg)
ESECUZIONE(CodiceReg,TitoloCanz,Anno)
AUTORE(Nome,TitoloCanzone)
CANTANTE(NomeCantante,CodiceReg)
"""


--n3. I cantanti che non hanno mai registrato una canzone come solisti

SELECT c.NomeCantante, COUNT(c.NomeCantante)
FROM CANTANTE c, ESECUZIONE e, 
WHERE c.CodiceReg = e.CodiceReg
GROUP BY e.TitoloCanzone
HAVING COUNT(c.NomeCantante) > 1;

--n3. versione diversa
SELECT c.NomeCantante 
FROM CANTANTE c, ESECUZION e 
WHERE c.CodiceReg = e.CodiceReg AND (
    SELECT COUNT(c.NomeCantante)
    FROM CANTANTE c, ESECUZIONE e, 
    WHERE c.CodiceReg = e.CodiceReg
    GROUP BY e.TitoloCanzone
    HAVING COUNT(c.NomeCantante) < 1);


--n3. versione diversa
SELECT c.NomeCantante 
FROM CANTANTE c, ESECUZIONE e 
WHERE c.CodiceReg = e.CodiceReg 
and NomeCantante NOT IN (
    SELECT c.NomeCantante
    FROM CANTANTE c, ESECUZIONE e, 
    WHERE c.CodiceReg = e.CodiceReg
    GROUP BY c.NomeCantante
    HAVING COUNT(c.NomeCantante) > 1);

--n4. I cantanti che hanno registrato canzoni sempre come solisti

SELECT e.TitoloCanz, COUNT(c.NomeCantante)
FROM (CANTANTE c, ESECUZIONE e, 
WHERE c.CodiceReg = e.CodiceReg
GROUP BY e.TitoloCanzone
HAVING COUNT(c.NomeCantante) < 2;

--n4. versione diversa

SELECT NomeCantante
FROM CANTANTE c
WHERE NomeCantante =  NOT IN  (
    SELECT e.TitoloCanz, COUNT(c.NomeCantante)
    FROM (CANTANTE c, ESECUZIONE e, 
    WHERE c.CodiceReg = e.CodiceReg
    GROUP BY e.TitoloCanzone
    HAVING COUNT(c.NomeCantante) >= 2;
);

--n4. versione diversa

SELECT NomeCantante
FROM CANTANTE
WHERE NomeCantante NOT IN (
    SELECT NomeCantante 
    FROM CANTANTE c, ESECUZIONE e,CANTANTE c1
    WHERE c.CodiceReg =  e.CodiceReg AND
          c.NomeCantante <> c1.NomeCantante
);

--n4. versione diversa

SELECT NomeCantante
FROM cantante c, esecuzione e
WHERE c.CodiceReg = e.CodiceReg
GROUP BY NomeCantante
HAVING COUNT(distinct c.NomeCantante <2);