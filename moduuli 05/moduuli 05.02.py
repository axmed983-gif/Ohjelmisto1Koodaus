luvut = []

while True:
    syote = input("anna luku")
    if syote == "":
        break
    luku= float(syote)
    luvut.append(luku)
    luvut.sort (reverse=True)
