from sys import stdin


def instancia(num):
    nomeMenor = ""
    notaMenor = 11
    num = int(num)
    while num > 0:
        nome, nota = input().split()
        nota = int(nota)
        if (nota < notaMenor) or (nota == notaMenor and nome > nomeMenor):
            notaMenor = nota
            nomeMenor = nome
        num -= 1
    return nomeMenor

k = 0
for line in stdin:
    k += 1
    inst = instancia(line)
    print('Instancia ' + str(k))
    print(inst)
    print()
