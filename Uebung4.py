liste   = list(range(-5,5))
print(liste)

# 7. Erstellen Sie eine neue Liste zahlen mit den ganzen Zahlen im Intervall [-4;3]. 
# Sortieren Sie die Liste anschließend aufsteigend nach dem Betrag der Elemente. (Ergebnis: [0,-1,1,-2,2,-3,3,-4]) 
# Hinweis: Python bietet die Funktion abs() zur Berechnung des Betrags einer Zahl.

liste.sort(reverse=True)
print(liste)

liste.sort(key=abs)
print(liste)


# 8. Erstellen Sie eine Liste einkaufsliste mit den Elementen "Äpfel", "Birnen", "Orangen", "Bananen".
einkaufsliste=['Äpfel', 'Birnen', 'Orangen', 'Bananen']
print(einkaufsliste)
print("")

# 9. Fügen Sie an die erste Position (Index 0) sowie zwischen den bereits bestehenden Elementen jeweils ein neues Element mit dem Wert "Schokolade" ein. 
# Hinweis: Zur Lösung dieser Aufgabe ist die Verwendung einer Schleife notwendig 
# (Papier und Bleistift können hilfreich sein, um herauszufinden an welche Positionen der Liste die „Schokolade“ einzufügen ist). 
# (Ergebnis: ['Schokolade', 'Äpfel', 'Schokolade', 'Birnen', 'Schokolade', 'Orangen', 'Schokolade', 'Bananen'])

print(len(einkaufsliste))
i=0
while i <= len(einkaufsliste):
    einkaufsliste.insert(i, "Schokolade")
    i+=2
print(einkaufsliste)
print("")

# 10. Ersetzten Sie das erste Element von einkaufsliste durch den Wert "Erdnüsse". 
# (Ergebnis: ['Erdnüsse', 'Äpfel', 'Schokolade', 'Birnen', 'Schokolade', 'Orangen', 'Schokolade', 'Bananen'])
einkaufsliste[0] = "Erdnüsse"
print(einkaufsliste)
print("")

# 11. Löschen Sie, angefangen mit der Löschung des ersten Elements (Index 0), jedes zweite Element von einkaufsliste. 
# (Ergebnis: ['Äpfel', 'Birnen', 'Orangen', 'Bananen'])
del einkaufsliste[::2]
print(einkaufsliste)
print("")

# 12. Erstellen Sie eine neue Liste einkaufsliste2 als Kopie von einkaufsliste.
einkaufsliste2 = einkaufsliste.copy


# 14. Geben Sie die Einträge der einkaufsliste der Reihe nach aus (angefangen vom Element mit dem Index 0 bis zum letzten Element) 
# und entfernen Sie dabei das jeweils ausgegebene Element aus der Liste.

while einkaufsliste: 
    print(einkaufsliste.pop(0), "wird entfernt")
    

print(einkaufsliste)