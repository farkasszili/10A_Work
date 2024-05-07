a = str(input("Kérem a tippjeit szóközzel elválasztva (pl. 16 45 8): "))

lista = a.split(" ")

ossz = 0
for i in lista:
    ossz = ossz + 1

if ossz < 5:
    print("Nem adtál meg elég számot!")
    exit(0)

if ossz > 5:
    print("Túl sok számot adtál meg!")
    exit(0)

print("Tovább")
