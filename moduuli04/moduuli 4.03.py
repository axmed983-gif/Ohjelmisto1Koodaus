import math

pienin = math.inf
suurin = math.inf

syote = input ( " anna luku: ")

while syote != pienin:
    luku = int(syote)

    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku

    syote = input ( " anna luku: ")

