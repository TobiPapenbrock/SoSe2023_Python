text_1 = "Hallo Welt!"
text_2 = "FOM"
tupel = (1,2,3,4,5,6,7,8,9,10)                                                          # entspricht: tupel = tuple(range(1, 11))
liste_1 = [1,2,3,4,5,6,7,8,9,10] 
liste_2 = [6,7,8,9,10,11,12,13,14,15] 
zahl_1 = 6
zahl_2 = 12

# 1. Geben Sie aus, wie viele Elemente in text_1 und tupel enthalten sind.
print(len(text_1), "Anz. Elemente von text_1")
print(len(tupel), "Anz. Elemente von tupel")
print("")

# 2. Geben Sie jeweils das erste Element von text_1, und tupel aus. 
# Geben Sie jeweils das letzte Element von text_1, und tupel aus.

print(text_1[0], "Erstes Element von text_1")
print(text_1[-1], "Letztes Element von text_1")

print(tupel[0], "Erstes Element von Tupel ")
print(tupel[-1], "Letztes Element von Tupel")
print("")

# 3. Geben Sie die drei ersten Elemente von text_1 und tupel aus. 
# Geben Sie die drei letzten Elemente von text_1 und tupel aus.

print("Erste 3 Elemente von text_1: ", text_1[:3])
print("Letzte 3 Elemente von text_1:", text_1[-3:])

print("Erste 3 Elemente von tupel: ", tupel[:3])
print("Letzte 3 Elemente von tupel: ", tupel[-3:])
print("")

# 4. Geben Sie jedes zweite Element von liste_1 aus.
print(liste_1[::2])
print("")

# 5. Geben Sie das größte Element von text_1 u. das kleinste von liste_2 aus.
print(max(text_1))
print(min(liste_2))
print("")

# 6. Fügen Sie die Elemente aus liste_1 zweimal an die ursprünglich liste_1 an und geben Sie die liste über print(liste_1) aus.
liste_1*=3
print(liste_1)

# 7. Generieren Sie eine neue Liste (gesamtliste) mit allen Elementen aus tupel, liste_1 und liste_2. 
# Geben Sie die Gesamtliste sowie die Anzahl der Elemente der Gesamtliste aus. Tipp: 
# Erzeugen Sie zunächst die Verbindung aus den beiden Listen liste_1 und liste_2 und fügen Sie anschließend die Elemente aus tupel hinzu.


gesamtliste = list(tupel) +liste_1 + liste_2
print(len(gesamtliste))
print("")

# 8. Geben Sie an, ob zahl_1 in der Gesamtliste vorkommt oder nicht.
if zahl_1 in gesamtliste:
    print("Jawollo")
else:
    print("Schade Banane")

# 9. Geben Sie die Position des ersten Auftretens von zahl_1 in der Gesamtliste an. 
# Die Position soll dabei der tatsächlichen Position entsprechen (das erste Element der Liste hat die Position 1). 
# Falls die zahl_1 nicht in der Gesamtliste vorkommt, soll eine entsprechende Meldung ausgegeben werden.
if zahl_1 in gesamtliste:
    print(gesamtliste.index(zahl_1)+1)
else:
    print("Meldung")



# 10. Geben Sie an, wie oft zahl_1 in der Gesamtliste vorkommt.


# 11. Geben Sie den Index für jedes Element in Gesamtliste an, an der der Wert von zahl_1 steht.


# 12. Erstellen Sie eine neue Variable (text) deren Inhalt sich aus dem erste Wort von text_1, einem anschließenden Leerzeichen 
# und dem gesamten Inhalt von text_2 sowie einem abschließenden „!“ zusammensetzt. Geben Sie die Variable über print(text) aus.
print(text_1)
print(text_2)
text = text_1[:text_1.index(" ")+1] + text_2
print(text)
