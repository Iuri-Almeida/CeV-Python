ex = ' Exercício 075 '
print(f'{ex:=^31}')

# n1 = int(input('Primeiro valor: '))
# n2 = int(input('Segundo valor: '))
# n3 = int(input('Terceiro valor: '))
# n4 = int(input('Quarto valor: '))
tupla = (int(input('Primeiro valor: ')), int(input('Segundo valor: ')),
        int(input('Terceiro valor: ')), int(input('Quarto valor: ')))
print(f'Vc digitou os valores {tupla}')
pares = ''
for i in tupla:
    if (i % 2) == 0:
        pares += ' ' + str(i)
pares = pares.split()
pares = ", ".join(pares)
valor3 = f'apareceu na {tupla.index(3) + 1}˚' if tupla.count(3) != 0 else 'não foi digitado em nenhuma'
print(f'\nA) O 9 aparece {tupla.count(9)} vezes.')
print(f'B) O valor 3 {valor3} posição.')
print(f'C) Os valores pares digitados foram: {pares}.')
