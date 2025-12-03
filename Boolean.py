#Scrivi un programma che chieda quanti anni hai e se hai la patente
#Il programma risponde se puoi guidare (età sopra i 18 e hai la patente)
età = int(input('quanti anni hai?'))
patente = input('hai la patente? si/no')

guida = età > 18 and patente == 'si'
print(guida)

#un utente puo entrare in biblioteca se:
#non è in ritardo con la consegna dei libri
#se ha un abbonamento premium
#date due variabili, l'utente puo entrare se non è in ritardo e ha l'abbonamento
ritardo = 18.00
consegna = float(input('orario consegna libro ?(es. 10.00)'))
abbonamento = input('hai un abbonamento premium? si/no')

permesso = consegna <= 18.00 and abbonamento == 'si'
print(permesso)