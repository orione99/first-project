#esercizio 1
lista = ['Giovanni','Erika','Paola','Simone','Andrea','Davide']
for i,val in enumerate(lista):
    print(i,val)

#esercizio 2
#calcolatore di numeri inseriti
somma = 0
numeri = input('inserisci una serie d numeri: ')
for i in numeri:
    i = int(i)
    somma += i
print(somma)

#esercizio 3
#calcolatore di parole
somma = 0
parola = ''
frase = input('scrivi una frase: ')
for carattere in frase:
    if carattere != ' ':
        parola += carattere
    else:
        if parola != '':
            somma += 1
            parola = ''
if parola != '':
    somma += 1
print(somma)

#esercizio 4
#prendo i numeri dispari
numeri = input('inserisci alcuni numeri: ')
for i in numeri:
    i = int(i)
    if i % 2 == 1:
        print(i)

