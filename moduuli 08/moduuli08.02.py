import mysql.connector

def hae_kentan_tiedot(icao)
    sql = f"SELECT name, municipality FROM airport where ident = {icao}"

yhteys = mysql.connector.connect(
    host = "127.0.0.1"
    port = 3306
    database = "airport"
    user = "root"
    password = "root"
    autocommit = True


icao_koodi = input("Anna kentän ICAO-koodi: ")
haen_kenan_tiedot (icao_koodi)

kursori.execute (sql)
tulos = kursori-fetchall()
if kursori.rowcunt > 0:
   for rivi in tulos:
       print

