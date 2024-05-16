'''
2)Készítsen programot, mely kiírja a felhasználó hatoslottó számait a ”lotto6.txt” fájl-ba.
A hatoslottó játék során 45 db számból (1-45) sorsolnak ki 6 db-ot. A játékosok ebből az intervallumból tippelnek meg 6 egész számot.
Kérje be a felhasználótól egyesével a tippjeit, s ezeket a számokat tárolja el egy lis-tában.
A lista elemeit növekvő sorrendben írja ki a fent megadott fájlba.	
'''
import random
cv = 1
lottoszamok=[]
x = open("lotto6.txt", "w")
while cv<=6:
      szam = int(input("Add meg egy tippedet:"))
      lottoszamok.append(szam)
      x.write(str(szam)+"\t")
      cv= cv+1

x.close()      
print(sorted(lottoszamok))

sorsolas=[]
talalat =0
cv=0
while cv<6:
      sorsoltszam= random.randrange(1, 46)
      sorsolas.append(sorsoltszam)
      if sorsoltszam in lottoszamok:
            talalat= talalat+1
      cv = cv+1
print(sorted(sorsolas))
print("Találatok száma: ", talalat)

input()




