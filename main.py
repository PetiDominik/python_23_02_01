# megoldás
def eredmeny(jatekosPontjai: list[int], gepPontjai: list[int]) -> str:
    if pontOsszeg(jatekosPontjai) > 21:
        return "Játékos veszített"
    elif pontOsszeg(gepPontjai) > 21:
        return "Gép veszített"

def pontOsszeg(lista: list[int]) -> int:
    osszeg = 0
    for ertek in lista:
        osszeg += ertek
    return osszeg
# teszteset
def jatekos_vesztett_teszt():
    jatekosPontok: list[int] = [11, 11]
    gepPontok: list[int] = [11, 10]

    print("Teszteset 1. [Játékos veszített | Túlcsorbul]\n\t", end="")
    kapott: str = eredmeny(jatekosPontok, gepPontok)
    vart: str = "Játékos veszített"
    if kapott == vart:
        print("A teszteset sikeres!")
    else:
        print("A teszteset sikertelen!")

def jatekos_vesztett_teszt2():
    jatekosPontok: list[int] = [11, 2, 5]
    gepPontok: list[int] = [11, 5, 4]

    print("Teszteset 2. [Játékos veszített]\n\t", end="")
    kapott: str = eredmeny(jatekosPontok, gepPontok)
    vart: str = "Játékos veszített"
    if kapott == vart:
        print("A teszteset sikeres!")
    else:
        print("A teszteset sikertelen!")

def jatekos_vesztett_teszt3():
    jatekosPontok: list[int] = [11, 5, 4]
    gepPontok: list[int] = [11, 9]

    print("Teszteset 3. [Játékos veszített | Több lap]\n\t", end="")
    kapott: str = eredmeny(jatekosPontok, gepPontok)
    vart: str = "Játékos veszített"
    if kapott == vart:
        print("A teszteset sikeres!")
    else:
        print("A teszteset sikertelen!")


def gep_vesztett_teszt():
    jatekosPontok: list[int] = [11, 10]
    gepPontok: list[int] = [11, 11]

    print("Teszteset 4. [Gép veszített | Túlcsorbul]\n\t", end="")
    kapott: str = eredmeny(jatekosPontok, gepPontok)
    vart: str = "Gép veszített"
    if kapott == vart:
        print("A teszteset sikeres!")
    else:
        print("A teszteset sikertelen!")

def gep_vesztett_teszt2():
    jatekosPontok: list[int] = [11, 4, 5]
    gepPontok: list[int] = [11, 5, 3]

    print("Teszteset 5. [Gép veszített]\n\t", end="")
    kapott: str = eredmeny(jatekosPontok, gepPontok)
    vart: str = "Gép veszített"
    if kapott == vart:
        print("A teszteset sikeres!")
    else:
        print("A teszteset sikertelen!")

def gep_vesztett_teszt3():
    jatekosPontok: list[int] = [11, 9]
    gepPontok: list[int] = [11, 4, 5]

    print("Teszteset 6. [Gép veszített | Több lap]\n\t", end="")
    kapott: str = eredmeny(jatekosPontok, gepPontok)
    vart: str = "Gép veszített"
    if kapott == vart:
        print("A teszteset sikeres!")
    else:
        print("A teszteset sikertelen!")

def dontetlen_teszt():
    jatekosPontok: list[int] = [11, 10]
    gepPontok: list[int] = [11, 10]

    print("Teszteset 7. [Döntetlen]\n\t", end="")
    kapott: str = eredmeny(jatekosPontok, gepPontok)
    vart: str = "Döntetlen"
    if kapott == vart:
        print("A teszteset sikeres!")
    else:
        print("A teszteset sikertelen!")

def dontetlen_teszt2():
    jatekosPontok: list[int] = [11, 5, 6]
    gepPontok: list[int] = [11, 6, 5]

    print("Teszteset 8. [Döntetlen | Túlcsorbul mindkettő]\n\t", end="")
    kapott: str = eredmeny(jatekosPontok, gepPontok)
    vart: str = "Döntetlen"
    if kapott == vart:
        print("A teszteset sikeres!")
    else:
        print("A teszteset sikertelen!")


def tesztek():
    jatekos_vesztett_teszt()
    jatekos_vesztett_teszt2()
    jatekos_vesztett_teszt3()
    gep_vesztett_teszt()
    gep_vesztett_teszt2()
    gep_vesztett_teszt3()
    dontetlen_teszt()
    dontetlen_teszt2()


tesztek()