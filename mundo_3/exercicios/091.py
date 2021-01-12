from time import sleep
from random import randint
from operator import itemgetter
ex = ' Exercício 091 '
print(f'{ex:=^31}')

dicionario = {}
print('Valores sorteados:')
for i in range(1, 5):
    dado = randint(1, 6)
    print(f'    O jogador{i} tirou {dado}')
    dicionario[f'jogador{i}'] = dado
    sleep(1)
print('Ranking dos jogadores:')
# ranking = sorted(dicionario.items(), key = lambda x: x[1], reverse = True)
ranking = sorted(dicionario.items(), key = itemgetter(1), reverse = True)
for i, j in enumerate(ranking):
    print(f'    {i + 1}˚ lugar: {j[0]} com {j[1]}')
    sleep(1)
