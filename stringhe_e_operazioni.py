#input di una frase e la sua scrittura inversa
frase = input('scrivi uan frase')
inverso = frase[::-1]
print(inverso)

#contollo se la frase è palindroma
print(frase == frase[::-1])

# Esercizio 1 

testo = 'Giovanni'
print("Primo carattere:", testo[0])     
print("Ultimo carattere:", testo[-1])   


# Esercizio 2

testo = 'InFoRmAtIcA'
print(testo.upper())  
print(testo.lower())  


# Esercizio 3

testo = 'Giovanni'
lettera = 'n'
conteggio = testo.count(lettera)
print(f"La lettera '{lettera}' compare {conteggio} volte.")  


# Esercizio 4

testo = 'io abito a Pistoia'
print(testo.startswith('i'))  
print(testo.endswith('a'))    


# Esercizio 5 

testo = 'Python'
print(testo[::-1]) 


# Esercizio 6 

testo = '   Io mi chiamo Giovanni   '
print(testo.strip())  


# Esercizio 7

parola = 'programmazione'
print(testo[:3] * 3)  
