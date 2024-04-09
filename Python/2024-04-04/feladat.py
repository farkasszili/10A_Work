x = 0
try:
    x = int(input("Kérek egy egész számot: "))
except:
    print("Nem egy egész számot adtál meg!")

if int(x):
    if x % 2 == 0:
        print("Páros szám (" + str(x) + ")")
    else:
        print("Páratlan szám (" + str(x) + ")")
