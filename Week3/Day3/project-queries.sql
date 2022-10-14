-- n1 prodotti piu' venduti
-- ordini da utenti in partita iva
-- ordini da utenti registrati alla newsletter
-- ordini da milano
-- ordini per anno o mese
-- prodotti piu acquistati a milano 
-- categoria piu' ordinata 
-- giorno con maggiori acquisti nella settimana 


-- gli utenti iscritti alla newsletter che hanno fatto almeno 1 acquisto 
select distinct u.nome,u.cognome
from utente u, ordine o 
where u.uid = o.uid and newsletter = 1;

-- raggruppa gli ordini per città 


-- città con il maggior numero di ordini 
select distinct i.citta, count(o.uid) as NumeroOrdini
from ordine o, indirizzo i
where i.uid = o.uid 
group by i.citta;


-- numero di ordini che contiene nome prodotto che contiene %notebook 

select * 
from utente 
where nome like 'da%';

select * 
from prodotto 
where nome like 'notebook%';

-- quanti ordini di computer abbiamo avuto 
SELECT op.quantita, op.prezzo
FROM prodotto AS p 
INNER JOIN orpr01 AS op
	ON (p.pid = op.pid)
INNER JOIN ordine AS o
	ON (op.oid = o.oid)  
WHERE op.quantita >1
Group by op.quantita,op.prezzo;

-- fai una SUM delle quantità raggruppando per nome prodotto

-- il carrello maggiore 
SELECT max(op.prezzo)
FROM prodotto AS p 
INNER JOIN orpr01 AS op
	ON (p.pid = op.pid)
INNER JOIN ordine AS o
	ON (op.oid = o.oid)  
WHERE op.quantita >1
having max(op.prezzo);


-- il cliente con l'ordine con carrello maggiore 
SELECT u.nome, u.cognome, op.prezzo
FROM utente AS u
INNER JOIN ordine AS o
	ON (u.uid = o.uid )
INNER JOIN orpr01 AS op
	ON (o.oid = op.pid)
where op.prezzo >1;


