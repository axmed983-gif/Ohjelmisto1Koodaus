import random
# parametrinen funktio, joka palauttaa satunnaisen nopan silmäluvun 1-6
def heita_noppaa():
    return random.randint(1,6)

#pääohjelma
if __name__ == '__main__':
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = heita_noppaa()
        print(silmaluku)