import os 

#--- Datei Öffnen ---
dateiname = "NASA_access_log_Jul95.txt"

#--- Datei öffnen ---
try: 
    dat_obj = open(dateiname, "r")
    print("Datei geoeffnet")
except(IOError) as e: 
    print("Fehler", e.args[1])
    os._exit(1)
log = []
for zeile in dat_obj:
    neueZeile = zeile.strip()
    log.append(neueZeile)
    print(neueZeile)

# Alternative 
#with open(dateiname, "r") as dat_obj: 
#    log=dat_obj.readlines()

dat_obj.close()


#log=[ 
#    '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245',
#    '199.12.110.3 - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985',
#    '199.120.110.21 - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/mission.html HTTP/1.0" 200 4085',
#    'unicomp6.unicomp.net - - [01/Jul/1995:00:00:11 -0400] "GET /countdown/liftoff.html HTTP/1.0" 304 0',
#    '199.120.110.21 - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/missions/small.gif HTTP/1.0" 200 4179',
#    'unicomp6.unicomp.net - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logos.gif HTTP/1.0" 304 0',
#    '192.120.110.21 - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/video/livevideo.gif HTTP/1.0" 200 0'
#]

#eine_zeile=log[0]
#print(eine_zeile)

# x=eine_zeile.split()
# print(x)

log_info=[] # strurierten Infos wer, wann, was

for eine_zeile in log:

    x=eine_zeile.split()

    ip_adresse=x[0]
    print("IP:", ip_adresse)

    seite=x[6]
    print("Seite:", seite)

    uhrzeit=x[3]
    uhrzeit=uhrzeit[13:]
    print("Zeit:", uhrzeit)

    log_info.append( [ip_adresse,seite,uhrzeit] )

dateiname2 ="output.txt"
try: 
    dat_obj.open = (dateiname2, "w")
    print("Datei nochmal geöffnet")
except (IOError) as e: 
    print("Fehler")
    os._exit[1]


dat_obj.write("="*10)
#print(log_info)
dat_obj.write("3 Logzeile, Seite:", log_info[2][0], log_info[2][1], log_info[2][2])
dat_obj.write("="*10)

i=0
for zeile in log_info:
    i+=1
    dat_obj(i,zeile)
# oder
for nr,zeile in enumerate(log_info,1):
    dat_obj.write(nr,zeile)

dat_obj.obj("="*80)

fstring="| {0:25} | {1:35} | {2:10} |"
for zeile in log_info:
    dat_obj.write(fstring.format(zeile[0],zeile[1],zeile[2]))

dat_obj.write("="*80)



