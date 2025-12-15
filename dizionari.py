#definiamo un dizionario studente con chiavi e valori
studente = {'nome' : 'Giovanni', 'età' : 25, 'corso' : 'informatica'}

#modifichiamo valore 'età'
studente['età'] = 26

#aggiungiamo chiave e valore per 'matricola'
studente['matricola'] = 821999

#recuperiamo un valore con get e stampiamo
nome = studente.get('nome','nessun valore')
print(nome)

#iteriamo per chiave e valore e stampiamo
for k, v in studente.items():
    print(k,v)

##prove aggiuntive
#aggiungiamo altre chiavi e valori
studente['cognome'] = 'Mazzotta'
studente['anno di nascita'] = '8 Febbraio 1999'

#verifichiamo se esiste una chiave senno la creiamo
studente.setdefault('città','Pistoia')
print(studente)

#creiamo una nuova chiave con valore e poi la cancelliamo con .pop()
studente['voto'] = 28
print(studente)
studente.pop('voto')
print(studente)

#svuotiamo il nostro dizionario con .clear()
studente.clear()
print(studente)
