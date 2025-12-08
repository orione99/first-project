#definisco n come base 0
n = 0

#creo un ciclo while dove chiedo il valore di n
#se n maggiore di 0 stampo e interrompo senno il ciclo si ripete
while n <= 0:
    n = int(input('inserisci un numero'))
print(n)

#calcola la somma delle cifre di un numero:
#numero = input('inserisci un numero: ')
somma = 0
for cifra in numero:
    somma += int(cifra)
print('la somma delle cifre è : ',somma)


##piccolo gioco creato al momento
#indovina la risposta giusta
risposta1 = '1492'
risposta2 = 'Firenze'
risposta3= 'Turing'
risposta1 = ''
risposta2 = ''
risposta3 = ''

while risposta1 != '1492':
    print('in che anno è stata scoperta l america?')
while risposta2 != 'Firenze':
    print('quale è il capoluogo della Toscana?')
while risposta3 != 'Turing':
    print('chi è considerato il padre fondatore dell informatica?') 
print('complimenti hai risposto a tutte le domande')

##Ho creato un piccolo quiz su tre domande
#Indovina la risposta giusta
print('BENVENUTO, INDOVINA QUESTE 3 DOMANDE DI CULTURA GENERALE !')
giocare = 'si'
while giocare == 'si':
    risposta1 = ''
    risposta2 = ''
    risposta3 = ''
    while risposta1 != '1492':
        risposta1 = input('In che anno è stata scoperta l america?')
        if risposta1 == '1492':
            print('Bravo 1 su 3, prossima domanda')
        else:
            print('Risposta sbagliata, riprova')    
    while risposta2 != 'Firenze':
        risposta2 = input('Quale è il capoluogo della Toscana?')
        if risposta2 == 'Firenze':
            print('Ci siamo quasi 2 su 3')
        else:
            print('Risposta sbagliata, riprova')  
    while risposta3 != 'Turing':
        risposta3 = input('Chi è considerato il padre fondatore dell informatica?') 
        if risposta3 == 'Turing':
            print('Complimenti 3 su 3, hai completato il gioco')
        else:
            print('Risposta sbagliata, riprova')
     
    scelta = input('Vuoi ricomnicare? ').lower()
    if scelta == 'si':
        giocare = 'si'
        print('Ok, riiniziamo')
    elif scelta == 'no':
        print('Ok, arrivederci')
    else:
        print('Non ho capito')
