def speichern_ergebnis(verlauf):
    with open("verlauf.txt", "a") as datei:
        for rechnung in verlauf:
            datei.write(rechnung + "\n")
