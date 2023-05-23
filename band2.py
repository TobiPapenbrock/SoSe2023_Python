#ToDo: Datei "band.txt" auslesen 
dateiname = "band.txt"

with open(dateiname) as datObj:
    for zeile in datObj:
        print(zeile.rstrip())

# ToDo splitten nach ; 
inhalt=[]
with open(dateiname) as datObj:
    for zeile in datObj:
        print(zeile.rstrip())
        inhalt.append(zeile.rstrip().split(';'))
        print(inhalt)
        print("Vorname:", inhalt[0])


# ToDo einzelne Namen ausgeben Vorname: Angus Nachname: Young Instrument: Gitarre 
