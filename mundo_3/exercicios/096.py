ex = ' Exercício 096 '
print(f'{ex:=^31}')

def área(l, c):
    print(f'A área do seu terreno {l}x{c} é de {(l * c)}m².')


print('   Controle de Terrono   ')
print('-' * 25)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)
