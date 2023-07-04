import requests

url="https://topinfo.de/beispiele/kontaktformular.php"
values={'fullname': 'Karl Klammer', 
        'mailadress':'webmaster@fom.de', 
        'message':'Hallo Welt!'}
#req=requests.post(url, values)

i = 1
while i==1: 
    req=requests.post(url, values)
    
    if req:
        print(req.text)
    else:
        print("Fehler!")
    i+=1