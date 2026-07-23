def rechnen(zahl1, zahl2, operator):
    if operator == "+":
        return zahl1 + zahl2
    elif operator == "-":
        return zahl1 - zahl2
    elif operator == "*":
        return zahl1 * zahl2
    elif operator == "/":
        if zahl2 == 0:
            return "Fehler: Division durch 0"
        return zahl1 / zahl2
    else:
        return "Das war kein gültiger Operator!"