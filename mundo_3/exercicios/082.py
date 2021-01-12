ex = ' Exercício 082 '
print(f'{ex:=^31}')

lista = []
lista_par = []
lista_impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for num in lista:
    if (num % 2) == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
print('-=-' * 20)
print(f'A lista principal é: {lista}.')
print(f'A lista só com números pares é: {lista_par}.')
print(f'A lista só com números ímpares é: {lista_impar}.')
