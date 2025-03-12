print("Anche print è una funzione built-in")

print("Inserisci il tuo nome")

Nome=input()

print("Ciao", Nome)

Saldo= 1000

print("Quanto desideri prelevare ?")
prelievo = int(input())

if prelievo > 500:
    print("Mi spiace, non puoi prelevare più di 500")

else:
    if prelievo > Saldo:
        print("Mi dispiace ma il tuo saldo è insufficiente")

    else:
        Saldo -= prelievo
        print("Il tuo saldo attuale è", Saldo)