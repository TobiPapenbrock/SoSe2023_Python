import random

# Initialisierung
geheimzahl  = \
    random.randint(0,
                    100)
eingabe     = 0
zaehler     = 0
max_versuche= 5

print(geheimzahl)
# Schleifenkopf und Schleifenkoerper
while eingabe != geheimzahl and max_versuche >zaehler:
    eingabe = int(input("Ganze Zahl eingeben: "))


    if eingabe < geheimzahl:
        print("Zahl zu klein")

    if eingabe > geheimzahl:
        print("Zahl zu groß")

    zaehler = zaehler +1


if eingabe!=geheimzahl:
    print("Falsch du Idiot!")
else:
    print ("Richtig! Sie haben", zaehler, "Versuche benötigt.")