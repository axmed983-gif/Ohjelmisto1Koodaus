sukupuoli = int(input("valitse numero sukupuolesi mukaan, 1 on nainen ja 2 on mies: "))

if sukupuoli == 1:
    hemoglobiini = int(input("anna hemoglobiiniarvo:"))
    if hemoglobiini < 117:
        print("hemoglobiiniarvo on liian alhainen.")
    elif hemoglobiini > 175:
        print("hemoglobiiniarvo on korkea.")
    else:
        print("hemoglobiiniarvo on normaali")

if sukupuoli == 2:
    hemoglobiini = int(input("anna hemoglobiiniarvo:"))
    if hemoglobiini < 134:
        print("hemoglobiiniarvo on liian alhainen.")
    elif hemoglobiini > 195:
        print("hemoglobiiniarvo on korkea.")
    else:
        print("hemoglobiiniarvo on normaali")