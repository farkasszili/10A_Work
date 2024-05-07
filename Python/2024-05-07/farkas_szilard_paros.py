try:
    a = int(input("Kérek egy egész számot: "))

    if a % 2:
        print(f"Páratlan szám ({a})")
    else:
        print(f"Páros szám ({a})")
except:
    print("Nem egész számot adtál meg!")