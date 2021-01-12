ex = ' Exercício 093 '
print(f'{ex:=^31}')

jogador = dict()
jogador['Nome'] = str(input('Nome: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
jogador['Gols'] = []
for jogos in range(partidas):
    jogador['Gols'].append(int(input(f'  Quantidade de gols na partida {jogos + 1}: ')))
jogador['Total'] = sum(jogador['Gols'])
print('-=-' * 14)
print(jogador)
print('-=-' * 14)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-' * 14)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for i, j in enumerate(jogador['Gols']):
    print(f'    => Na partida {i + 1}, fez {j} gols.')
print(f'Foi um total de {jogador["Total"]}')
