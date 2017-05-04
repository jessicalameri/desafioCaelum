from sys import stdin


def converteLetra(letra):
    if ord(letra) <= ord('Z'):
        return ord(letra) - (ord('A') - 1) + 26
    else:
        return ord(letra) - (ord('a') - 1)


def soma(palavra):
    somatorio = 0
    palavra = palavra.strip()
    for letra in palavra:
        somatorio += converteLetra(letra)

    return somatorio


def ehPrimo(somatorio):
    for i in range(2, somatorio):
        if somatorio % i == 0:
            return "It is not a prime word."
    return "It is a prime word."

for line in stdin:
    print (ehPrimo(soma(line)))
