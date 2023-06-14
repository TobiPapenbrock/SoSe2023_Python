import re

text=" der die das, wer wie was!"

# r für "raw", damit Backslash geht + \s für Leerzeichen . für Wildcard er für Bestandteil des Wortes 
matchi=re.match(r"\s.er", text)
print(matchi)
print(matchi.group())

#print(re.matchi("der", text))

# Suche 1. Wort, welches mit "w" beginnt und 2 weitere, beliebige Zeichen hat. Groß/Kleinschreibung wird ignoriert (durch flags=re.I).
regexobj=re.compile(r"w..", flags=re.I)
matchi=regexobj.search(text)
print(matchi.group())

matchi = re.search(r"w..", text, flags=re.I)
print(matchi.group())



test2="91+3 ist 12"
#matchi = re.search(r"\d*.\d*", test2)
matchi = re.search(r"(\d*)(.)(\d*)", test2)
print(matchi.group(1))
print(matchi.group(2))
print(matchi.group(3))
