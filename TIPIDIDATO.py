# Esistono i seguenti tipo di dato: String, Number (Integer, floats), boolean
print("questa e una stringa")
print("2") #anche questa e una stringa
print(2) #questo e un integer (e un numero intero)
print(2.0) #questo e un float(e un numero con la virgola)
print(0.0000000001)
print(True) #questo e un boolean
print(False)

#questi sotto si chiamano operatori di confronto. tutte le volte che uso un operatore di confronto produco un boolean. gli operatori di confronto sono : > ; < ; <= ; >= ; !;
print(1 < 2) #true
print(3 > 5) #false

#esempio
print("voglio fare un calcolo matematico semplice")

print(1+2) #integer
print(3+1) #integer
print(4*5) #integer
print(10/5) #Float
#il fatto che il linguaggio decida per noi il tipo di dato piu adeguato determina il fatto che siamo si di fronte ad un linguaggio debolmente tipizzato


print(2.5 + 1.3)
print(6.7 - 8.4)
print(4.2 * 2.3)
print(5.5 / 1.9)


#modulo %, anche chiamato resto della divisione
print(14 % 2)

print(1 ** 2)
print(8.0 // 3.0)
print(8.0 // 7.0)


#Usiamo le parentesi
print((5*2) + (8*3) - (10/2) *4)

#1. Le variabili devono avere delle denominazioni "parlanti", nel nome devo spiegarle il significato
#2. Non posso avere nodi con parole vietate for, if ,while, true, false ecc ecc ecc
#3. Le varibili sono dei contenitori di una informazione singola


#PascalCase
#UPPERCASE
#kebab-case
#camelCase

#ASSEGNO UNA VARIABILE
#nomeVariabile = valore
mioNome = "Serafim"
MiaEta = 18
corsi = 1
studenti = 18



#RICHIAMO UNA VARIABILE
print(mioNome)

#"Mescolo" una variabile con una stringa
print("ciao",  mioNome, "hai", MiaEta, "anni", "In questo momento segui", corsi, "corso" )


#Calcolo Matematico
voto_scritto= 60
voto_orale= 80





media1 = (voto_scritto + voto_orale)/2

print("questo è la media dello scritto e orale",round(media1))


personalizzazione= 75
inglese= 90
matematica= 70
database= 65
programmazione= 85
italiano= 75
sistemi= 100

media=(personalizzazione + inglese + matematica + database + programmazione + italiano + sistemi)/7


print("La media del mio esame è", round (media))



