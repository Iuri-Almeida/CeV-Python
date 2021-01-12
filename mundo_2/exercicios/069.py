ex = " Exercício 069 "
print(f'{ex:=^31}')

mais_18 = homem = mulher_20 = 0
pessoas = 1
while True:
    print(f'----- Pessoa {pessoas} -----')
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if i >= 18:
        mais_18 += 1
    if s == 'M':
        homem += 1
    if s == 'F' and i < 20:
        mulher_20 += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    pessoas += 1
    if r == 'N':
        break
print(f'\nA) Existem {mais_18} pessoas maiores de 18 anos.')
print(f'B) Existem {homem} homens que foram cadastrados.')
print(f'C) Existem {mulher_20} mulheres menores de 20 anos.')
