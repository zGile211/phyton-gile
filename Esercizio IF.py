print("Inserisci il tuo cognome per accetere al tuo conto")

Cognome= input()

Saldo= 1500

print("Benvenuto", Cognome, "il tuo saldo è di", Saldo )



print("Che operazione vuoi svolgere?")
print("1- Prelievo")
print("2- Deposito")
Operazione=int(input())


if Operazione == 1:
    print("Quanto vuoi prelevare?")
    Prelievo= int(input())
    if Prelievo <= Saldo and Prelievo <= 600:
        Saldo-=Prelievo
        print("Hai prelevato", Prelievo, "€. Il tuo saldo attuale è di", Saldo, "€.")
    elif Prelievo>=600:
        print("Mi diapiace non puoi ritirare più di 600€")
    else:
        print("Il tuo saldo è insufficiente")

elif Operazione == 2:
        print("Quanto vuoi depositare?")
        Deposito=int(input())
        Saldo+=Deposito
        print("Il tuo saldo attuale è di", Saldo, "€.")

