

text= """
Erwin Lindemann
Tel.: 0800/77889900
Fax: 0800/77889999 erwin.lindemann@epost.de (privat)
Lottoannahmestelle
Telefon 01803 / 12341234-11 Fax 01803 / 12341234-22 annahme@lotto.com
Herren-Boutique Erwin
Tel: 02232 222 - 3
Email: erwin@hbe-wuppertal.de (Geschäft)
"""

import re

# Nr. 7a
tel = re.findall(r"(Telefon|Tel)\.?:? (\d*)[ /]*(\d*) *-* *(\d*)", text)
print(tel)
telefonnummern=[]

for eintrag in tel:
    nummer=eintrag[1]
    nummer+="/"
    nummer+=eintrag[2]
    if eintrag[3]:
        nummer+="-"+eintrag[3]
    telefonnummern.append(nummer)

#print(nummer)
print(telefonnummern)


# Nr. 7b
# [^\s]+@[^\s]+ -> [^\s]+ alle Zeichen, welche keine Leerzeichen sind @ bis zum at, danach wieder [^\s] alle Zeichen des Texts, welche keine Leerzeichen sind
# 
mail = re.findall(r"[^\s]+@[^\s]+", text)

# Alternativ
mail = re.findall(r"[\w|.|-|_]+@[\w|.|-]+", text)
print(mail)


