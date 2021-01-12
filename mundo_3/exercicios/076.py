ex = ' Exercício 076 '
print(f'{ex:=^31}')

tupla = (
    'Pão', 2,
    'Leite', 5,
    'Arroz', 10,
    'Macarrão', 12,
    'Coca-Cola', 7,
    'Mouse', 85,
    'Monitor', 450,
    'Curso', 29
)
print('-=-' * 10)
print('{:^30}'.format(' Listagem de Preços '))
print('-=-' * 10)
for i in range(0, len(tupla), 2):
    print(f'{tupla[i]:.<21}R${tupla[i + 1]:>7.2f}')
print('-' * 30)