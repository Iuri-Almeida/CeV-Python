ex = ' Exercício 085 '
print(f'{ex:=^31}')

numeros = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite {i}˚ valor: '))
    if (n % 2) == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'\nOs valores pares em ordem crescente são: {numeros[0]}')
print(f'Os valores ímpares em ordem crescente são: {numeros[1]}')
