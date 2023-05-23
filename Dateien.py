import os

#--- Datei: Lesen & Schreibenb ---
dateiname = "testdatei.txt"

#--- Datei öffnen ---
try: 
    dat_obj = open(dateiname, "w")
    print("Datei geoeffnet")
except (IOError) as e: 
    print("Fehler ", e.args[1])
    os._exit(1)

#--- in Datei schreiben ---
for i in range(11): 
    dat_obj.write(str(i)+"\n")



dat_obj.write("Penis")
# --- Datei schließen
dat_obj.close()

#--- aus Datei lesen ---
dat_obj = open(dateiname, "r")

print("Ausgabe:")
for zeile in dat_obj:
    aktuelle_zeile = zeile.strip()
    print(aktuelle_zeile)

#--- Datei schließen ---
dat_obj.close()