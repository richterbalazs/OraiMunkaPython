import Renszarvas


def beolvas():
    lista = []
    beFajl = open("fajlok/Mikulasszan.txt", "r", encoding="utf-8")
    adatoklistaja = beFajl.readlines()
    print(adatoklistaja)
    for index in range(1, len(adatoklistaja), 1):
        if not("Santa Claus" in adatoklistaja[index]):
            daraboltsor = adatoklistaja[index].split(("@"))
            # print(daraboltsor)
            szarvas = Renszarvas.Renszarvas(daraboltsor[0], daraboltsor[1], daraboltsor[2], daraboltsor[3])
            # print(szarvas)
            lista.append(szarvas)
            # print(lista)

    beFajl.close()

    return lista

def angolMegfelelo(nev, lista):
    index = 0
    talalat = True
    while index < len(lista) and talalat:
        if lista[index].nevmagyar == nev:
            talalat = False
        index += 1

    if not (talalat):
        print(f"A szarvas angol neve: {lista[index - 1].nevangol}.")
    else:
        print("Nincsen ilyen rénszarvas")


def mikulasSzam(lista: list):
    db = 0
    index = 0
    while index < len(lista):
        daraboltLeiras = lista[index].leiras.split(" ")
        # print(daraboltLeiras)
        index2 = 0
        while index2 < len(daraboltLeiras):
            if daraboltLeiras[index2] == "Mikulás":
                db += 1
            index2 += 1
        index += 1
    print(f"A mikulás szó előfordulásának száma: {db}.")


def atlagMagassag(lista):
    osszeg = 0
    index = 0
    while index < len(lista):
        osszeg += lista[index].magassag
        index += 1

    if len(lista) == 0:
        print("Az átlag 0")
    else:
        atlag = osszeg / len(lista)
        print(f"a szarvasok átlag magassága: {atlag}")


def parosRepulo(lista):
    print("A páros helyen repülő szarvasok nevei: ", end="")
    index = 0
    while index < len(lista):
        if lista[index].hely % 2 == 0:
            print(lista[index].nevmagyar+" ", end="")
        index += 1
    print("")


def leghosszabbLeiras(lista):
    maxErtek = len(lista[0].leiras)
    maxIndex = 0
    index = 1
    while index < len(lista):
        if len(lista[index].leiras) > maxErtek:
            maxErtek = len(lista[index].leiras)
            maxIndex = index
        index += 1
    print(f"A leghosszabb leírás: {lista[maxIndex].nev}")


def hetes():
    szarvasoklistaja = beolvas()

    for szarvas in szarvasoklistaja:
        print(szarvas.kiir())

    print(f"A rénszarvasok száma: {len(szarvasoklistaja)}.")

    angolMegfelelo("Pompás", szarvasoklistaja)

    mikulasSzam(szarvasoklistaja)

    atlagMagassag(szarvasoklistaja)

    parosRepulo(szarvasoklistaja)

    leghosszabbLeiras(szarvasoklistaja)