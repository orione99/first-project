#Esercizio richiesto
#definisco la funzione 'media'
def media(*args):
    return int(sum(args) / len(args))
#stampo la media inserendo i dati da calcolare 
print(media(1,2,3,4,5,6,7,8,9))


#pratica delle funzioni
#creo una funzione per il lancio di un dado
#importo la libreria random
import random
def dado():
    return random.randint(1,6)

#assegno il valore 0 e creo un circuito con 'while' per farlo lanciare finche non esce 6
valore = 0
while valore != 6:
    valore = dado()
    if valore == 6:
        print('il valore è :', valore, 'ottimo !')
    else: 
        print('il valore è :', valore, 'riprovo')


#ricreo la stessa funzione ma con due dadi
#importo la libreria random e creo la funzione sommando i due dadi
import random
def dadi():
    return random.randint(1,6) + random.randint(1,6)

#creo nuovamente il circuito con 'while' finche la somma non è 9
somma_dadi = 0
while somma_dadi != 9:
    somma_dadi = dadi()
    if somma_dadi == 9:
        print('il risultato è :', somma_dadi,'ottimo !')
    else:
        print('il risultato è :', somma_dadi,'riprovo')

#creo una funzione dove legge la frase dell' input, split() della frase per rimuovere gli spazi tra le parole
#len() delle parole, riporta la somma delle parole
def somma_parole():
    x =input('scrivi una frase')
    parole = x.split()
    conteggio = len(parole)
    return print(conteggio)

somma_parole()

#creo una funzione che date due liste le trasforma in un dizonario k,v
def dizionario(x,y):
    diz = dict(zip(x,y))
    return print(diz)
y = [1,2,3,4,5]
x = ['uno', 'due', 'tre', 'quattro', 'cinque']

dizionario(x,y)

#creo uan funzione che lanci il dado 100 volte e fa la media dei valori usciti
def media_dadi():
    lanci_dadi = [random.randint(1,6)for _ in range(100)]
    media = sum(lanci_dadi) / len(lanci_dadi)
    return print(media)

media_dadi()

    