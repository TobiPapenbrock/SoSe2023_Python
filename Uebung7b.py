

def datum_einlesen():
    daten = [] #Tag, Monat, Jahr 
    
    try:
        tag=int(input("Bitte den Tag eingeben: "))
        daten+=tag,
    except ValueError:
        print("Es sind nur Zahlen erlaubt...Arschloch")
        daten+=1,
    
    try:
        monat = int(input("Bitte den Monat eingeben: "))
        daten+=monat,
    except ValueError: 
        print("Es sind nur Zahlen erlaubt...Arschloch")
        daten+=1,
    
    try:
        jahr = int(input("Bitte das Jahr eingeben: "))
        daten.append(jahr)
    
    except ValueError:
        print("Es sind nur Zahlen erlaubt...Arschloch")
        daten+=1,

    return daten

print("Bitte Datum eingeben: ")
datum=datum_einlesen()
print(datum)

t,m,j=datum_einlesen()
print(t,m,j)