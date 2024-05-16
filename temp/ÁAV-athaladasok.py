#2.b feladat:
def SzamolAthaladasok():
      print("A bejáratnál az áthaladások száma: ", len(bekilepesek))

#2.a feladat:
fk = open("athaladasok.txt")
bekilepesek = []
for x in fk:
      bekilepesek.append(x)                                       
      
#2.b feladat:   
SzamolAthaladasok()

#2.c feladat:
belepesek_szama = 0
for x in bekilepesek:
      egylepes = x.split(" ")
      if egylepes[0] == "1" and int(egylepes[2])<730:
            belepesek_szama = belepesek_szama + 1
print("Belépések száma: ", belepesek_szama)

