ex = ' Exercício 073 '
print(f'{ex:=^31}')

brasileirao = (
    'SAO',
    'CAM',
    'FLA',
    'INT',
    'GRE',
    'PAL',
    'FLU',
    'SAN',
    'COR',
    'CEA',
    'CAP',
    'ACG',
    'BGT',
    'FOR',
    'SPT',
    'BAH',
    'VAS',
    'GOI',
    'BOT',
    'CFC'
)

print('A) Os cinco primeiros são:')
for pos, time in enumerate(brasileirao[:5]):
    print(f'{pos + 1}˚: {time}, ', end = '')

print('\n\nB) Os últimos quatro colocados são:')
for pos, time in enumerate(brasileirao[-4:]):
    print(f'{pos + 17}˚: {time}, ', end = '')

print('\n\nC) Lista com os times em ordem alfabética:')
print(f'{sorted(brasileirao)}')

print('\nD) Em que posição da tabela está o Flamengo? ')
print(f'O Flamengo está em {brasileirao.index("FLA") + 1}˚.')
