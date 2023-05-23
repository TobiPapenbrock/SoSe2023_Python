
#log=[
#    '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245', 
#    '199.12.110.3 - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985',
#    '199.120.110.21 - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/mission.html HTTP/1.0" 200 4085', 
#    'unicomp6.unicomp.net - - [01/Jul/1995:00:00:11 -0400] "GET /countdown/liftoff.html HTTP/1.0" 304 0', 
#    '199.120.110.21 - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/missions/small.gif HTTP/1.0" 200 4179', 
#    'unicomp6.unicomp.net - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logos.gif HTTP/1.0" 304 0', 
#    '192.120.110.21 - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/video/livevideo.gif HTTP/1.0" 200 0'
#]
dateiname="NASA_access_log_Jul95.txt"
dateiname2="ausgabe.txt"
dat_Obj =open(dateiname, "r")
log=[]
print("Geöffnet")
for zeile in dat_Obj:
    neueZeile=zeile.strip()
    log.append(neueZeile)

dat_Obj.close()
# 1. a) Kopieren Sie die oben dargestellte Liste „log“ in ein neues Programm loganalyse.py. 
# Diese Liste ist ein Auszug der ersten sieben Zeilen der Webserver-Logdatei1 eines NASA-Servers. 
# Eine Element entspricht dabei einer Zeile – das muss für eine genauere Analyse noch optimiert werden.


# 1. b) Geben Sie die Anzahl der Zeilen (Listenelemente) sowie die Inhalte der ersten fünf Zeilen (Listenelemente) auf dem Bildschirm aus.

print(len(log))
print(log[0:4])
print("")


# 2. Erstellen Sie auf der Basis der Liste log eine neue Liste log_info mit der folgenden Struktur: [[wer, wann, was], [wer, wann, was], ...]
# wer: IP-Adresse oder Domain-Name
# wann: Uhrzeit (ohne Angabe des -- immer gleichen -- Datums)
# was: Name der aufgerufenen Datei bzw. des aufgerufenen Verzeichnisses
# Bsp.: [ ['199.72.81.55', '00:00:01', 'history/apollo'], [...], ...]


log_info = []

for eine_zeile in log: 
    eine_zeile = log[0]
    x = eine_zeile.split()
    ip_addr = x[0]
    seite = x[6]
    uhrzeit = x[3]
    uhrzeit = uhrzeit[13:]
    log_info.append([ip_addr, seite, uhrzeit])

print("="*10)
print(log_info)
print("3. Zeile: ",log_info[2][0], log_info[2][1], log_info[2][2])

#3. Geben Sie die ersten fünf Einträge von log_info nummeriert in der folgenden Form auf dem
#Bildschirm aus:
# 1 ['199.72.81.55', '00:00:01', '/history/apollo/']
# 2 ['unicomp6.unicomp.net', '00:00:06', '/shuttle/countdown/']


i = 0
#for zeile in log_info:
#    i+=1
#    print(i, zeile)

# oder 
for nr, zeile in enumerate(log_info, i):
    print(nr, zeile)

# 4. Die Log-Informationen der ersten fünf Zeilen sollen nun in Form einer Tabelle (s.u.) ausgegeben werden. 
# Die Spaltenbreite soll sich am jeweils längsten Element der Spalte orientieren (so dass keine 'Verschiebungen' auftreten können).
dat_Obj=open(dateiname2, "w")
fstring = "| {0:25} | {1:35} | {2:10} |"
dat_Obj.write("-"*80)
dat_Obj.write(fstring.format("wer", "wann", "was"))
dat_Obj.write("-"*80)
i=0
for zeile in log_info:
    dat_Obj.write(fstring.format(zeile[0], zeile[1], zeile[2]))
dat_Obj.write("-"*80)