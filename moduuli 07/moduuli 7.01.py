# vuoden ajat monikkoina ( kuukausi 1-12 )
vuodenajat = (
    "talvi"
    "talvi"
    "kevät"
    "kevät"
    "kevät"
    "kesä"
    "kesä"
    "kesä"
    "syksy"
    "syksy"
    "syksy"
    "talvi"
)
kuukausi = int(input("anna kuukauden numero (1-12): "))
if 1 <= kuukausi <= 12:
    print("vuodenaika on:", vuodenajat[kuukausi-1])
else:
    print("virheellinen kuukauden numero.")




