
bekert = int(input("Kérek egy egész számot: "))

if bekert < 10:
    print("A szám ("+str(bekert)+") Kisebb 10-nél")
elif bekert == 10:
    print("A szám (" + str(bekert) + ") Egyenlő 10-el")
else:
    print("A szám (" + str(bekert) + ") Nagyobb 10-nél")

exit(0)
