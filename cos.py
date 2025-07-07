zmmiene = []

def dodaj_zmienna(nazwa):
    for zm in zmmiene:
        if zm[0] == nazwa:
            return
    zmmiene.append([nazwa, len(zmmiene)])

def gdzie_zmienna(nazwa):
    for idx, zm in enumerate(zmmiene):
        if zm[0] == nazwa:
            return idx
    return -1

dodaj_zmienna("zmmiena")
dodaj_zmienna("zmmiena2")

print(gdzie_zmienna("zmienna"))

print(zmmiene)
