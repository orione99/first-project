#Esercizio 1
tuples = [(10, 15), (30,35), (20,25)]
ordinati = sorted(tuples, key = lambda x: x[1]) 
print(ordinati)

#Esercizio 2
t = (10, 23, 30, 45, 50, 67)
pari = tuple([x for x in t if x % 2 == 0])
print(pari)

#Esercizio 3
t = (8, 18, 11, 17, 21)
invertita = tuple(reversed(t))
print(invertita)

#Esrcizio 4
s = 'pitone'
t = tuple(set(s))
print(t)

#Esercizio 5
lista1 = [8, 17, 21, 24]
lista2 = ['g', 'p', 'a', 'm']
zipped = list(zip(lista1, lista2))
print(zipped)

#Esercizio 6
A = {'a', 'b', 'c'}
B = {'b', 'd', 'e'}
C = {'d', 'f', 'g'}
differenziale = A ^ B ^ C
print(differenziale)

#Esercizio 7
frase = 'oggi sto studiando oggi vado fuori'
uniche = set(frase.split())
print(uniche)

#Rsercizio 8
liste = [[10, 20, 30], [40, 30, 50], [60, 40]]
unione = set().union(*map(set, liste))
print(unione)
