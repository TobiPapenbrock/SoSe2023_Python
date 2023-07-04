import requests
import re

url="https://de.wikipedia.org/wiki/Leonardo_da_Vinci"
req = requests.get(url)
zeilen=req.text.splitlines()
bilder=[]

# HTML Tag: <img ... src="...">
for line in zeilen: 
    if "<img" in line:
        print(line)
        #erg=re.search(r"src=\S*\/\S*\.jpg", line)
        erg=re.search(r"src=\"(.+?)\.jpg\"", line)
        if erg:
            print("Erg.: ", erg.group(1))
            bild="https:"+erg.group(1)+".jpg"
            bilder.append(bild)
            print("-"*50)
        
print('\x1b[6;30;42m'+bild+'\x1b[0m'+" gefunden, beginne download")
zaehler=0

for bild in bilder:
    dateiname="img/bild_"+str(zaehler)+".jpg"
    dat_obj=open(dateiname, "wb")
    req=requests.get(bild)
    dat_obj.write(req.content)
    dat_obj.close
    zaehler+=1