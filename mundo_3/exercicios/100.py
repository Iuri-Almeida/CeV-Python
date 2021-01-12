from random import randint
from time import sleep
print(f'{" Exercício 100 ":=^31}')

def sorteia(l):
    print('Sorteando 5 valores da lista: ', end = '')
    for _ in range(5):
        v = randint(0, 10)
        l.append(v)
        print(v, end = ' ', flush = True)
        sleep(0.5)
    print('Pronto!')


def somaPar(l):
    s = 0
    for i in l:
        if (i % 2) == 0:
            s += i
    print(f'A soma entre os valores pares da lista {l} é {s}.')


números = []
sorteia(números)
somaPar(números)
