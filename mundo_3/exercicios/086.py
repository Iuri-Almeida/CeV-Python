ex = ' Exercício 086 '
print(f'{ex:=^31}')

matriz = []
for i in range(1, 4):
    linha = []
    for j in range(1, 4):
        linha.append(int(input(f'Digite o valor da posição {i}x{j} da matriz: ')))
    matriz.append(linha[:])
print('-=-' * 14)
for k in matriz:
    print(f'[ {k[0]:^3} ][ {k[1]:^3} ][ {k[2]:^3} ]')
