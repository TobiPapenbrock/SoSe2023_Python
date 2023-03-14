
# Initialisierung 
anzahl          = int(input("Bitte die Anzahl eingeben: "))
einzel_preis    = float(input("Bitte den Einzelpreis eingeben:"))
rabatt          = 0

summe = anzahl * einzel_preis

if anzahl >= 31:
    rabatt = 0.04
elif anzahl > 16 and anzahl < 30:
    rabatt = 0.03
elif anzahl > 6 and anzahl < 15:
    rabatt = 0.02
else:
    rabatt = 0

summe = summe - (summe * rabatt)

print("Das kostet in der Summe", summe, "€")
print("Mit einem Rabatt von", summe * rabatt, "€")