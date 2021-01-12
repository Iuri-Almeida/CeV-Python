ex = ' Exercício 095 '
print(f'{ex:=^31}')

jogadores = []
while True:
    print(f'----- {len(jogadores) + 1}˚ Jogador -----')
    jogador = dict()
    jogador['Nome'] = str(input('Nome: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    jogador['Gols'] = []
    for jogos in range(partidas):
        jogador['Gols'].append(int(input(f'Quantidade de gols na partida {jogos + 1}? ')))
    jogador['Total'] = sum(jogador['Gols'])
    jogadores.append(jogador.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 21)
print(f'{"Cod.":<4} {"Nome":<10} {"Gols":<15} {"Total":<5}')
print('-' * 37)
for j, v in enumerate(jogadores):
    print(f'{j:<4} {v["Nome"]:<10} {str(v["Gols"]):<15} {v["Total"]:<5}')
while True:
    print('-' * 37)
    opc = int(input('Mostrar os dados de qual jogador? (999 para interromper) '))
    while opc >= len(jogadores) and opc != 999:
        print(f'Erro! Não existe jogador com código {opc}! Tente novamente.')
        print('-' * 37)
        opc = int(input('Mostrar os dados de qual jogador? (999 para interromper) '))
    if opc == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opc]["Nome"]}:')
    for g, k in enumerate(jogadores[opc]['Gols']):
        print(f'    No jogo {g + 1} fez {k} gols.')
print('<< VOLTE SEMPRE >>')
