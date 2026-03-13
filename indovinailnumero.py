import random

def main():
    numero_segreto = random.randint(1, 100)
    max_tentativi = 6

    print("Ho scelto un numero tra 1 e 100.")

    for i in range(1, max_tentativi + 1):
        tentativo = int(input(f"Tentativo {i}/{max_tentativi}: inserisci un numero: "))

        if tentativo < numero_segreto:
            print("Troppo piccolo!")
        elif tentativo > numero_segreto:
            print("Troppo grande!")
        else:
            print(f"Bravo! Hai indovinato in {i} tentativi!")
            return

    print(f"Hai perso! Il numero segreto era {numero_segreto}.")

if __name__ == "__main__":
    main()
