## Descrizione del caso di studio

Storia
Revolut è una piattaforma finanziaria globale, supportata da un’app che consente in ogni momento di gestire le tue finanza con un semplice smartphone. Revolut Ltd è una società fintech, con sede nel Regno Unito fondata nel 2015. Tuttavia, già nel 2018 ha raggiunto lo status di unicorno. Con ciò si intende che è stata valutata più di un miliardo di dollari. La società ha realizzato un conto corrente multivaluta. 

A partire dal 2021 ha ottenuto la licenza bancaria anche in Italia dove viene riconosciuta a tutti gli effetti come una banca, dando quindi accesso ad un vero e proprio conto corrente. Tuttavia, esso non dà IBAN italiano, ma l’estensione LT è riconosciuta nell’area SEPA, cioè dei pagamenti europei. Revolut offre una carta di debito prepagata che consente di prelevare denaro (in valuta locale) in oltre 120 paesi del mondo.

Caso
Dal 2021 ha iniziato a concedere prestiti e credito al consumo direttamente online ai propri clienti direttamente tramite l’app proprietaria. 
La suddetta analisi dei requisiti è necessaria per la progettazione di uno strumento per le analisi, valutazione e miglioria del modello già utilizzato da Revolut, in particolare si propone di:
Migliorare il modello di credit scoring do Revolut Bank per migliorare l’efficacia con cui concede credito ai suoi clienti 
Poter analizzare e predire tramite dei modelli di ML quali dei suoi clienti potrebbe voler richiedere del credito. 
Poter analizzare e predire il default rate dei clienti che ha già ottenuto il credito. 
Predire quali e quando i clienti potrebbero aver necessità di credito per i loro acquisti e fornire i dati al team marketing per migliorare le leads performance


Analisi e raccolta dei requisiti 
Il modello di credit risk di Revolut attuale utilizzato dalla banca calcola in base ai soli dati in possesso ( età,sesso,disponibilità di denaro 
in conto corrente, se si è proprietari di immobile o in affitto, la professione che si svolge, la quantità di denaro richiesta, il tipo di aquisto che si vuole fare con il credito e la durata del credito) se concedere o meno il credito. 
Per la creazione del progetto di analisi per la banca Revolut il team Data & Technology della società di consulenza Epicode Consulting ha raccolto i dati seguenti:

* `1` Migliorare il modello di credit scoring do Revolut Bank per migliorare l’efficacia con cui concede credito ai suoi clienti
* `2` Poter analizzare e predire tramite dei modelli di ML quali dei suoi clienti potrebbe voler richiedere del credito. 
* `3` Poter analizzare e predire il default rate dei clienti che ha già ottenuto il credito. 
* `4` Predire quali e quando i clienti potrebbero aver necessità di credito per i loro acquisti e fornire i dati al team marketing per migliorare le leads performance

### Indice
- Descrizione del caso di studio
- 2. Storia
- 3. Caso
- Analisi e raccolta dei requisiti
- 1. Requisiti per la Banca
- 2. Requisiti per le Transazioni
- 3. Requisiti per i dati dell’Agenzia delle entrate
- 4. Team necessario Data & Technology
- Glossario dei termini
- 1. Tipologia di dati
- 2. Dati Revolut Bank
- 3. Dati transazioni-pagamenti online e offline
- 4. Dati Agenzia delle entrate
- 5. Implementazione
- Supporto alle decisioni aziendali
- 1. Storia/Infografica
- 2. Analisi Aggiuntive Proposte
- 3. Possibili implementazioni future

## Analisi e raccolta dei requisiti 
Il modello di credit risk di Revolut attuale utilizzato dalla banca calcola in base ai soli dati in possesso ( età,sesso,disponibilità di denaro in conto corrente, se si è proprietari di immobile o in affitto, la professione che si svolge, la quantità di denaro richiesta, il tipo di aquisto che si vuole fare con il credito e la durata del credito) se concedere o meno il credito. 
Per la creazione del progetto di analisi per la banca Revolut il team Data & Technology della società di consulenza Epicode Consulting ha raccolto i dati seguenti:

| dataset        | formato      | dimensione     | link fonte    | descrizione |
| ------------- |:-------------:| :-------------:|:-------------|:-------------|
|dataset_bank.csv| CSV | 10 | api.revolut.com/bankdata/| Dataset della banca sui clienti che hanno richiesto un credito e risultato del credit score |
| dataset_fiscalagency.json | JSON      |   10 | api.agenziaentrate.gov.it/portale/ | Dataset dell’agenzia delle entrate sui dieci clienti che hanno richiesto il credito |
| dataset_transactions.xml |  XML      |    10 | api.stripe.com/bank/37475859 | Dataset creato da azienda di credito terza su tutti i pagamenti online e offline effettuati |
