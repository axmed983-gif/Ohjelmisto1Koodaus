lentoasemat= {"somalia,suomi,ruotsi"}
while True:
    toiminto= input("valitse toiminto(uusi, haku, lopeta): ")
    if toiminto == "uusi":
        icao: str = input("anna lentoaseman icao-koodi: ")
        nimi= input("anna lentoaseman nimi: ")
        lentoasemat [icao] = "somalia,suomi,ruotsi"
     elif toiminto == "haku":        " "
        icao = input("anna haettava icao-koodi: ")
    if icao in lentoasemat:
        print "somalia,suomi,ruotsi:", lentoasemat[icao]
    else:
        print("lentoasema ei löutunyt.")
     elif toiminto == "lopeta:"
         print("lentoasema ei löytynyt.")
         break
     else:
         print("virheellinen valinta.")







        

