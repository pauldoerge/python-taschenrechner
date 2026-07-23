def eingabe_zahl(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Das war keine Zahl, probiers nochmal!")
def nächster_schritt():
    next_step = input("Was nun? ( (N)eue Rechnung, (V)erlauf, (B)eenden, (S)peichern  ")
    next_step = next_step.upper()
    return next_step