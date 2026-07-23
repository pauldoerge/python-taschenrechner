import sys
from rechner import rechnen
from eingaben import eingabe_zahl,nächster_schritt
from speichern import speichern_ergebnis

datei = open("verlauf.txt","r")
text = datei.read()
datei.close()

print("Bisheriger Verlauf: " + "\n" + text)

print("Taschenrechner")
verlauf = []
while True:

    erste_zahl = eingabe_zahl("Erste Zahl: ")
    eingabe_operator = input("Operator (+ - * /): ")
    zweite_zahl = eingabe_zahl("Zweite Zahl: ")



    if eingabe_operator in ["*","+","-","/"]:
        ergebnis = rechnen(erste_zahl, zweite_zahl, eingabe_operator)
        rechnung = f" {erste_zahl} {eingabe_operator} {zweite_zahl} = {ergebnis}"
        print(f"Ergebnis: {ergebnis}")
        verlauf.append(rechnung)

        while True:
            next_step = nächster_schritt()
            if next_step == "N":
                print("Auf ein neues!")
                break
            elif next_step == "V":

                with open("verlauf.txt", "r") as datei:
                    text = datei.read()
                    print(text)

                for rechnung in verlauf:
                    print(rechnung)
                print("Hier dein Verlauf!")
            elif next_step == "B":
                print("Du willst schon gehen? Nagut, tschö!")
                sys.exit()
            elif next_step == "S":
                if len(verlauf) == 0:
                    print("Nichts zu speichern!")
                else:
                    speichern_ergebnis(verlauf)
                    verlauf.clear()
                    print("Alles gespeichert!")
            else:
                print("Keine Auswahlmöglichkeit, probiers nochmal!")

    else:
        print("Das war kein gültiger Operator!")
