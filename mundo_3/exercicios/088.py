from random import randint
from time import sleep
ex = ' Exercício 088 '
print(f'{ex:=^31}')

jogos = int(input('Vai jogar quantas vezes? '))
palpites = []
for _ in range(jogos):
    palpite = []
    for _ in range(6):
        n = randint(1, 60)
        while n in palpite:
            n = randint(1, 60)
        palpite.append(n)
    palpites.append(palpite[:])
print('-=-' * 14)
for pos, palp in enumerate(palpites):
    palp.sort()
    print(f'Palpite {pos + 1}: {palp}')
    sleep(0.5)
