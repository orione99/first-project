#Esercizio 1
A = {'Giovanni', 'Erika', 'Paola'}
B = {'Giovanni', 'Paola', 'Paco'}
print('Entrambi :', A & B)
print('Solo A :', A - B)
print('Unici :', len( A | B))

#Esercizio 2
import random
lista_pari = []
lista_dispari = []
numeri = {random.randint(1,100) for _ in range(5)}
for n in numeri:
    if n % 2 == 0:
        lista_pari.append(n)
    else:
        lista_dispari.append(n)
    
print(numeri)
print(lista_pari, lista_dispari)

#Esercizio 3
frase = 'Eva dava l uva ad Ava Ava dava le uova ad Eva ora Eva è priva d uva mentre Ava è priva d uova'
parole = frase.split()
conteggio = {}
for p in parole:
    conteggio[p] = conteggio.get(p,0) + 1
print(conteggio)

#Esercizio 4
diz = {'tre' : 3, 'due': 2,'uno': 1}
inverso = {v : k for k, v in diz.items()}
print(inverso)

#Esercizio 5
Chiavi = ['Nome', 'Eta', 'Città']
Valori = ['Giovanni', 26, 'Pistoia']
diz = dict(zip(Chiavi, Valori))
print(diz)

#Esercizio 6
Parole = ['Accetta', 'l', 'opinione', 'di', 'tutti', 'ma', 'fa,' 'un', 'uso', 'parsimonioso', 'del', 'tuo', 'giudizio']
Gruppi = {}
for p in Parole:
    Gruppi.setdefault(len(p), []).append(p)
print(Gruppi)

#Esercizio 7
Parola = 'supercalifragilistichespiralidoso'
freq = {}
for c in Parola:
    freq[c] = freq.get(c,0) +1
print(freq)