ex = ' Exercício 087 '
print(f'{ex:=^31}')

matriz = []
soma_pares = soma_col_3 = 0
for i in range(1, 4):
    linha = []
    for j in range(1, 4):
        n = int(input(f'Digite o valor da posição {i}x{j} da matriz: '))
        soma_pares += n if (n % 2) == 0 else 0
        linha.append(n)
    matriz.append(linha[:])
for i in range(3):
    soma_col_3 += matriz[i][2]
print('-=-' * 14)
for k in matriz:
    print(f'[ {k[0]} ][ {k[1]} ][ {k[2]} ]')
print('-=-' * 14)
print(f'A) A soma dos valores pares digitados é: {soma_pares}.')
print(f'B) A soma dos valores da terceira coluna é: {soma_col_3}.')
print(f'C) O maior valor da segunda linha é: {max(matriz[1])}.')
