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