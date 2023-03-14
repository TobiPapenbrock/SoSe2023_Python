
# Initialisierung 
anzahl          = int(input("Bitte die Anzahl eingeben: "))
einzel_preis    = float(input("Bitte den Einzelpreis eingeben:"))
farbe           = input("Welche Farbe: ")
rabatt          = 0

summe = anzahl * einzel_preis
print(summe)

#Berechnung Rabatte abhängig von der Mänge 
if anzahl >=40 and anzahl % 10 == 0:
    rabatt = 0.95
elif anzahl >= 31 and einzel_preis > 10:
    rabatt = 0.96
elif anzahl > 16:
    rabatt = 0.97
elif anzahl > 6:
    rabatt = 0.98
else:
    rabatt = 0

#Berechnung Rabatte abhängig von der Farbe 

if farbe == "rot" or farbe =="blau":
    summe*=0.9

summe = summe * rabatt
#alternativ summe*=rabatt

print("Das kostet in der Summe", summe, "€")
print("Mit einem Rabatt von", summe * rabatt, "€")