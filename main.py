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

    kapott: str = eredmeny(jatekosPontok, gepPontok)
    vart: str = "Játékos veszített"
    if kapott == vart:
        print("A teszteset sikeres!")
    else:
        print("A teszteset sikertelen!")

def gep_vesztett_teszt():
    jatekosPontok: list[int] = [11, 10]
    gepPontok: list[int] = [11, 11]

    kapott: str = eredmeny(jatekosPontok, gepPontok)
    vart: str = "Gép veszített"
    if kapott == vart:
        print("A teszteset sikeres!")
    else:
        print("A teszteset sikertelen!")

def dontetlen():
    jatekosPontok: list[int] = [11, 10]
    gepPontok: list[int] = [11, 10]

    kapott: str = eredmeny(jatekosPontok, gepPontok)
    vart: str = "Döntetlen"
    if kapott == vart:
        print("A teszteset sikeres!")
    else:
        print("A teszteset sikertelen!")


def tesztek():
    jatekos_vesztett_teszt()
    gep_vesztett_teszt()
    dontetlen()


tesztek()