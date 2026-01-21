kuha = int(input("anna kuhan pituus (cm): "))

if kuha < 37:
    puuttuu = 37 - kuha
    print("kuhan pituus on vähemmän kuin 37cm palauta veteen, kuhasta puuttuu",  int(puuttuu), "cm")