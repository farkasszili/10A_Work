elso = str(input("Kérem az első gyümölcsöt: "))
masodik = str(input("Kérem a második gyümölcsöt: "))
harmadik = str(input("Kérem a harmadik gyümölcsöt: "))
negyedik = str(input("Kérem a negyedik gyümölcsöt: "))

temp = 0
temp_1 = ""
lista = [elso, masodik, harmadik, negyedik]

print("\n")
print("Lista: " + str(lista))

for i in lista:
    if len(i) > temp:
        temp = len(i)
        temp_1 = i

print("\n")
print("A leghosszabb: " + temp_1)
print("Karakterek száma: " + str(temp))

exit(0)
