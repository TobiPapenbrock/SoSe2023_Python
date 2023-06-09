import random
#  1. Erstellen Sie eine neue, nicht veränderbare Menge mit der Bezeichnung spielkugeln; 
# die Menge soll die ganzen Zahlen von 1 bis 49 enthalten.
spielkugeln = frozenset(range(1,50))

#2. Initialisieren Sie zwei neue Mengen: kugeln_in_trommel und kugeln_in_ablage. 
# Die Trommel soll zunächst alle Elemente aus spielkugeln erhalten; die Ablage ist zunächst leer.

kugeln_in_trommel = set(spielkugeln)
kugeln_in_ablage = set()

# 3. ‚Ziehen’ Sie nun zufällig sechs Zahlen aus der Menge der Trommel, und legen Sie diese in der Ablage ab 
# (nehmen Sie die entsprechenden Werte aus Trommel heraus). 
# Geben Sie über print die beiden Mengen sowie eine sortierte Liste mit den gezogenen Zahlen aus.

i = 0
zahl = 0
while i < 6: 
    zahl = random.sample(kugeln_in_trommel, 1)[0]
    kugeln_in_ablage.add(zahl)
    kugeln_in_trommel.remove(zahl)
    i+=1

#kugeln_in_ablage = random.sample(kugeln_in_trommel, 6)
#kugeln_in_trommel-=set(kugeln_in_ablage)

print(kugeln_in_ablage)
print("")
print(kugeln_in_trommel)

# 4. Im August 2017 finden insgesamt vier Ziehungen statt. Die Ziehungsdaten stehen in einem Tupel zur Verfügung:
history_ziehungen_erste_zahl = {"2017-Aug-05": 3,
                                "2017-Aug-12": 49,
                                "2017-Aug-19": 13}

history_ziehungen_alle_zahlen = {"2017-Aug-05": (4,3,5,6,7, 31,),
                                "2017-Aug-12": (1,2,3,4,5,6),
                                "2017-Aug-19": (21, 40, 1, 12, 33, 25)}

print("Was waren alle Zahlen am 12.8.2017? ", history_ziehungen_alle_zahlen["2017-Aug-12"])