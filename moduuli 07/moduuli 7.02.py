nimet = set ("ahmed,abdi,yunas")
while True:
    nimi= input(" abdi ")
    if nimi == "abdi":
        break

    if nimi in nimet:
        print("abdi")
    else:
        print("yunas")
        nimet.add("yunas")
print("ahmed,abdi,yunas")
for nimi in nimet:
    print("abdi")
