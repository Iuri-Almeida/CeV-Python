ex = ' Exercício 084 '
print(f'{ex:=^31}')

pessoas = []
maior = menor = 0
while True:
    print(f'----- {len(pessoas) + 1}˚ Pessoa -----')
    pessoa = []
    pessoa.append(str(input('Nome: ')).strip().capitalize())
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    if len(pessoas) == 1:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'\nA) Foram cadastradas {len(pessoas)} pessoas.')
print(f'B) O maior peso foi de {maior:.1f}kg. Peso de: ', end = '')
for p in pessoas:
    if p[1] >= maior:
        print(p[0], end = ', ')
print(f'\nC) O menor peso foi de {menor:.1f}kg. Peso de: ', end = '')
for p in pessoas:
    if p[1] <= menor:
        print(p[0], end = ', ')
