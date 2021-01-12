ex = ' Exercício 094 '
print(f'{ex:=^31}')

lista = []
while True:
    print(f'----- {len(lista) + 1}˚ pessoa -----')
    dic = {}
    dic['Nome'] = str(input('Nome: ')).strip().capitalize()
    dic['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    dic['Idade'] = int(input('Idade: '))
    lista.append(dic.copy())
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('Erro! Responda apenas S ou N.')
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 14)
print(f'A) Foram cadastradas {len(lista)} pessoas.')
soma_idade = 0
mulheres = []
for p in lista:
    soma_idade += p['Idade']
    if p['Sexo'] == 'F':
        mulheres.append(p['Nome'])
media = soma_idade / len(lista)
print(f'B) A média de idade do grupo é {media:.2f}.')
print(f'C) A lista com todas as mulheres é {mulheres}.')
maiores = []
for p in lista:
    if p['Idade'] > media:
        maiores.append(p)
print('D) A lista com todas as pessoas que estão acima da média:')
for pessoa in maiores:
    for k, v in pessoa.items():
        print(f'{k} = {v:<8}', end = ' ')
    print()
