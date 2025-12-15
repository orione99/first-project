#creiamo due corsi di laurea con i suoi studenti
corso_A = {'Marco', 'Giulia', 'Francesco', 'Giovanni', 'Michele'}
corso_B = {'Giulia', 'Giuseppe', 'Michele', 'Sara', 'Erika'}

#chi frequenta entramni i corsi
print(corso_A & corso_B)

#chi frequenta solo il corso A
print(corso_A - corso_B)

#chi frequenta solo il corso B
print(corso_B - corso_A)

#chi frequenta almeno un corso
print(corso_A | corso_B)

#quanti studenti unici ci sono in totale
studenti_unici = len(corso_A | corso_B)
print(studenti_unici)

##prove aggiuntive
#aggiungiamo uno studente al corso_A e un terzo corso: corso_C
corso_A.add('Luisa')
corso_C = {'Giulia', 'Giovanni', 'Marco', 'Andrea', 'Alice'}

#vediamo eventuali intersezioni e studenti unici
print(corso_A & corso_B & corso_C)
studenti_unici = len(corso_A | corso_B | corso_C)
print(studenti_unici)