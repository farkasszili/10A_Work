
my_year = int(input("Kérem a születési évedet: "))
other_year = int(input("Kérem a másik születési évét: "))

if my_year < other_year:
    print("Te idősebb vagy mint a másik.")
else:
    print("Te fiatalabb vagy mint a másik.")
print("\n")

my_weight = int(input("Kérem a súlyodat kg-ban: "))
other_weight = int(input("Kérem a másik súlyát kg-ban: "))

if my_weight > other_weight:
    print("Te testesebb vagy mint a másik.")
else:
    print("A másik testesebb mint te.")
print("\n")

my_name = str(input("Kérem a nevedet: "))
other_name = str(input("Kérem a másik nevét: "))

print("Neved: "+my_name)
print("Másik neve: "+other_name)


