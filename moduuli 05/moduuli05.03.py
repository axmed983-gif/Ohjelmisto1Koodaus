# kysytään kokonaisluku positiivinen kokonaisluku
käyttäjäluku= int(input("anna kokonaisluku? "))

# jaetaan käyttäjän antamaa arvoa 2,3,4... ( käyttäjäluku -1 ) se on jakaja
# jos, käyttäjän luku on jaollinen yhdelläkin jakajan arvolla, niin se käyttäjäluku ei ole alkuluku
# jos ei löydy yhtään jakajan arvoa, jolla käyttäjäluku on jaollinen käyttäjäluku on alkuluku
jakaja= 2
on_alkuluku=True

for jakaja in range (2,käyttäjäluku):
    if käyttäjäluku % jakaja == 0:
        on_alkuluku= False

if on_alkuluku == True:
    print("käyttäjäluku on alkuluku")
else:
    print( " käyttäjäluku ei ole alkuluku")

# oliko käyttäjäluku alkuluku vai ei ?

