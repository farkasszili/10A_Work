import random

a = str(input("Kérem a tippjeit szóközzel elválasztva (pl. 16 45 8): "))

lista = a.split(" ")
uj_lista = []

ossz = 0
for i in lista:
    ossz = ossz + 1

if ossz < 6:
    print("Nem adtál meg elég számot!")
    exit(0)

if ossz > 6:
    print("Túl sok számot adtál meg!")
    exit(0)


for i in lista:
    uj_lista.append(int(i))

uj_lista.sort()


file = open("tippek.txt", "w")
file.write(str(uj_lista))

# Masodik resze

random_lista = []
temp = 0
while temp < 6:
    temp = temp + 1
    random_lista.append(int(random.randint(1, 45)))

random_lista.sort()

correct_lista = 0

for i in uj_lista:
    for h in random_lista:
        if i == h:
            correct_lista = correct_lista + 1
            break


print("\n")
print("Talált számok: " + str(correct_lista))
print("\n")
print("Ön által megadott: " + str(uj_lista))
print("Gépi lista: " + str(random_lista))

