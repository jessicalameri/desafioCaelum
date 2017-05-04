from sys import stdin


def converte(linha):
    convertida = ""
    linha = linha.upper()
    for letra in linha:
        if letra == "A" or letra == "B" or letra == "C":
            convertida += "2"
        elif letra == "D" or letra == "E" or letra == "F":
            convertida += "3"
        elif letra == "G" or letra == "H" or letra == "I":
            convertida += "4"
        elif letra == "J" or letra == "K" or letra == "L":
            convertida += "5"
        elif letra == "M" or letra == "N" or letra == "O":
            convertida += "6"
        elif letra == "P" or letra == "Q" or letra == "R" or letra == "S":
            convertida += "7"
        elif letra == "T" or letra == "U" or letra == "V":
            convertida += "8"
        elif letra == "W" or letra == "X" or letra == "Y" or letra == "Z":
            convertida += "9"
        elif letra == "-" or letra == "1" or letra == "0":
            convertida += letra

    return convertida


for line in stdin:
    print(converte(line))
