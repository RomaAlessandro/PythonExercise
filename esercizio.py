studenti = ["", "", "", "", ""]
voti = [0, 0, 0, 0, 0]
somma = 0
num = 5

for i in range(num):
    studenti[i] = input("Nome: ")
    voti[i] = int(input("Voto: "))
    somma += voti[i]

media = somma / num

for i in range(num):
    print(studenti[i], "-", voti[i])

print("Media =", media)
