# Permetti al utente di inserire 2 numeri in teri e calcola il risultato delle 4 operazioni
# + - * / **

num1 = int(input("Inserisci un numero intero"))
num2 = int(input("Inserisci un altro numero intero"))

ADDIZZIONE= num1 + num2
SOTTRAZZIONE= num1 - num2
DIVISIONE= num1 / num2
MOLTIPLICAZIONE= num1 * num2
POTENZA1= num1 ** 2
POTENZA2= num2 ** 2 

print("Il risultato dell'addizione è:", ADDIZZIONE)
print("Il risultato della sottrazzione è:", SOTTRAZZIONE)
print("Il risultato dell'divisione è:", DIVISIONE)
print("Il risultato della moltiplicazione è:", MOLTIPLICAZIONE)
print("Il risultato della potenza è:", POTENZA1, POTENZA2)