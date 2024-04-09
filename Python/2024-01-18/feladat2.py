szoveg = input("Kérek egy szöveget: ")
print(szoveg.lower())
print(szoveg.upper())

print("\n")
szoveg2 = input("Kérek egy szót: ")
kicsi = szoveg2.lower()
nagy = szoveg2.upper()
print("Kicsi: "+kicsi)
print("Nagy: "+nagy)

print("\n")
szam = int(input("Kérek egy negatív számot: "))
if szam > 0:
    print("Nem negatív számot adtál meg!")
else:
    ertek = abs(szam)
    print("Abszolút értéke: " + str(ertek))

print("\n")
tizedes = float(input("Kérek egy tizedestört számot: "))
formatted = round(tizedes, 2)
print("Kerekítve: " + str(formatted))
