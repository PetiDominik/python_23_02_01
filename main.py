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

    print(eredmeny(jatekosPontok, gepPontok))

def tesztek():
    jatekos_vesztett_teszt()

tesztek()