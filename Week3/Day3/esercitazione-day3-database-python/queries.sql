
-- n1. I cantautori (persone che hanno cantato e scritto la stessa canzone) il cui nome inizia per 'D'

SELECT NomeCantante
FROM canzone, autore
WHERE autore.Nome = canzone.NomeCantante and NomeCantante LIKE 'D%';

-- n2. I titoli dei dischi che contengono canzoni di cui non si conosce l'anno di registrazione

SELECT d.TitoloAlbum AS Titolo
FROM disco d, contiene c, esecuzione e
WHERE d.NroSerie = c.NroSerieDisco AND c.CodiceReg = e.CodiceReg
AND e.Anno IS NULL;

-- n3. I cantanti che non hanno mai registrato una canzone come solisti

SELECT c.NomeCantante, COUNT(c.NomeCantante)
FROM CANZONE c, ESECUZIONE e
WHERE c.CodiceReg = e.CodiceReg
GROUP BY e.TitoloCanzone
HAVING COUNT(c.NomeCantante) > 1;

-- n3. versione diversa
SELECT c.NomeCantante
FROM CANZONE c, ESECUZION e
WHERE c.CodiceReg = e.CodiceReg AND (
    SELECT COUNT(c.NomeCantante)
    FROM CANZONE c, ESECUZIONE e
    WHERE c.CodiceReg = e.CodiceReg
    GROUP BY e.TitoloCanzone
    HAVING COUNT(c.NomeCantante) < 1);


-- n3. versione diversa
SELECT c.NomeCantante
FROM CANTANTE c, ESECUZIONE e
WHERE c.CodiceReg = e.CodiceReg
and NomeCantante NOT IN (
    SELECT c.NomeCantante
    FROM CANTANTE c, ESECUZIONE e
    WHERE c.CodiceReg = e.CodiceReg
    GROUP BY c.NomeCantante
    HAVING COUNT(c.NomeCantante) > 1);

-- n4. I cantanti che hanno registrato canzoni sempre come solisti

SELECT e.TitoloCanz, COUNT(c.NomeCantante)
FROM CANTANTE c, ESECUZIONE e
WHERE c.CodiceReg = e.CodiceReg
GROUP BY e.TitoloCanzone
HAVING COUNT(c.NomeCantante) < 2;

-- n4. versione diversa

SELECT c.NomeCantante
FROM CANZONE as c
WHERE NomeCantante NOT IN (
    SELECT NomeCantante
    FROM CANZONE c, ESECUZIONE e,CANZONE c1
    WHERE c.CodiceReg =  c1.CodiceReg AND
          c.NomeCantante <> c1.NomeCantante
);

-- n4. versione diversa

SELECT NomeCantante
FROM cantante c, esecuzione e
WHERE c.CodiceReg = e.CodiceReg
GROUP BY NomeCantante
HAVING COUNT(distinct c.NomeCantante <2);