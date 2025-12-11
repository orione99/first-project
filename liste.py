#creo una lista di numeri
numeri = [1,2,3,4,5,]

#aggiungo un numero alla fine e sostituisco il terzo
numeri.append(6)
numeri.insert(2,85)
print(numeri)

##qualche esercizio sulle liste
#creiamo una lista 
lista_spesa = ['latte','caffe','zucchero','pasta','sale','patatine']

#modifichiamo la lista
lista_spesa.sort()
lista_spesa.insert(4,'pane')
lista_A = []
lista_B = []
for alimento in lista_spesa:
    if alimento in ('pane', 'pasta','patatine','sale','caffe'):
        lista_A.append(alimento)
    else:
        lista_B.append(alimento)

print(lista_spesa)
print(lista_A)
print(lista_B)