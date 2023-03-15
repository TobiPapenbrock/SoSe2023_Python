eingabe=input("Bitte etwas eingeben ")
print("Laenge der Zeichenkette:",len(eingabe))
umfang="kurz"

if len(eingabe) <3:
    print("Ui Ui Ui, das sind ja weniger als 3 Zeichen. ")
    print("Toll, wie Du", len(eingabe)," Zeichen eingeben kannst")

elif len(eingabe)> 10: 
    print("Wow, Du Tier, deine Zeichenkette \x1B[3m",eingabe," \x1B[0m sind jetzt mehr als 10 Zeichen")
    print("Ich bin begeistert, wie Du", len(eingabe)," Zeichen eingegeben hast! Weiter So!")
    umfgang = "lang"

else: 
    print("Wow, Du Tier, deine Zeichenkette \x1B[3m",eingabe," \x1B[0m sind jetzt mehr als 3 Zeichen - aber kleiner als 10")
    print("Ich bin begeistert, wie Du", len(eingabe)," Zeichen eingegeben hast! Weiter So!")

    

print(umfang)