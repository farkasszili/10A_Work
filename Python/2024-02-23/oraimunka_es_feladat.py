container = []


def check(i):
    calc = i / 5
    if calc.is_integer():
        print("\nIgen, osztható 5-el.")
        container.append(i)
    else:
        print("\nNem, nem osztható 5-el, mivel a végeredmény (" + str(calc) + ") lett.")
    start()


def pre_check():
    in_num = int(input("\nKérek egy számot: "))
    check(in_num)


def list_container():
    print(container)
    start()


def search_container(i):
    try:
        print("\nA keresett szám: " + str(container[i]))
    except:
        print("\nNincsen ilyen a listában!")

    start()


def start():
    print("Lehetséges opciók:")
    print("1. Osztható-e 5-el")
    print("2. Lista kilistázása")
    print("3. Listában való keresés index-el")
    print("4. Kilépés\n")

    option = int(input("Kérem válasszon egy opciót: "))

    if option == 1:
        pre_check()
    elif option == 2:
        list_container()
    elif option == 3:
        search_container(int(input("Kérek egy lista indexet: ")))
    elif option == 4:
        exit(0)
    else:
        print("Nincsen ilyen opció")
        start()


start()
