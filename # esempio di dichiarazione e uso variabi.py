# esempio di dichiarazione e uso variabile
print("scrivi il tuo nome, caro utente!")

# per poter acquisire qualcosa che digita l'utente utilizzo la funzione input()
# nomeuser = "dario"
nomeuser = input() #argomento mancante

print("benvenuto", nomeuser)

# faccio la stessa cosa in modo più veloce passando come argomento all' input una frase
# funzione (argomento) --> tutto questo si chiama FIRMA del METODO
cognomeuser = input("scrivi il tuo cognome..")
print("il tuo cognome è", cognomeuser)


print("----------NUMERI----------")
# ATT: tutto cio che recupero da un altr utente è considerato una stringa, un testo. per poter fare 
# un calcolo devo fare il TYPE CASTING , ovvero forzare quella variabile ad essere un numero e non una stringa

num1 = input("scrivi un numero")
num2 = input("scrivi un altro numero")
somma = num1 +num2 
print("la somma vale: ", somma)
# esempio con int
num3 = int("3")
num4 = int("6")
somma2 = num3 + num4
print(somma2)