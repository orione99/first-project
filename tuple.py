#creiamo una lista con tre colori
#stampiamo primo ed ultimo elemento
colori = ('Rosso', 'Rosso', 'Verde')
print(colori[0], colori[-1])

#contiamo quante volte compare l'alemento 'rosso'
print(colori.count('Rosso'))

somma = 0
sport = ('Calcio', 'Basket', 'Tennis', 'Pallavolo', 'Rugby')
if 'Calcio' in sport:
    print('Il calcio è presente')
for i in sport:
    somma += 1
print(somma)