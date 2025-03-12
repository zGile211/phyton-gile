#ESERCIZIO 1
#Stampa il tuo nome e cognome in console, nel terminale. Specifica 2 variabili distinte e separate

mioNome= "Serafim"
mioCognome= "Dita"
print("Il mio nome è:",mioNome , mioCognome)

#ESERCIZIO 2
#Calcola l'area e il perimetro di un rettangolo avente base = 5.7 e altezza = 6.2

baseRettangolo= 5.7
altezzaRettangolo= 6.2

print("L'area del rettangolo è:",baseRettangolo*altezzaRettangolo)
print("Il perimetro del rettangolo è di:",baseRettangolo*2+altezzaRettangolo*2)

#ESERCIZIO 3
#Calcola l'area e il perimetro del seguente triangolo rettangolo lato1 = 9 lato2 = 12 lato3 = 15
#-Calcola il teorema secondo il quale la somma del quadrato sull'ipotenusa è uguale alla somme dei quadrati sui cateti
#-Calcola il teorema di pitagora

lato1= 9
lato2= 12
lato3= 15

print("L'area del triangolo è:",lato1*lato2/2 )
print("Il perimetro del triangolo è:",lato1+lato2+lato3)

print()

print()


#ESERCIZIO 4
#Calcola l'area e il perimetro di un cerchio di raggio 8.7
#(Usa entrambi i metodi per il calcolo della potenza)

raggioCerchio= 8.7

print("L'area del cerchio è di:", raggioCerchio**2*3.14)
print("Il perimetro del cerchio è:",2*3.14*raggioCerchio)
potenza=pow(raggioCerchio,2)
print("L'area del cerchio è di",potenza*3.14 )

print("Il perimetro del cerchio è", )