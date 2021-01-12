from random import randint
ex = ' Exercício 074 '
print(f'{ex:=^31}')

tupla = tuple(randint(0, 10) for _ in range(5))
print('Foram sorteados os valores: ', end = '')
for i in tupla:
    print(i, end = ' ')
# tupla = sorted(tupla)
# print(f'\nO menor valor gerado foi {tupla[0]}.')
# print(f'O maior valor gerado foi {tupla[-1]}.')
print(f'\nO maior valor gerado foi {max(tupla)}.')
print(f'O menor valor gerado foi {min(tupla)}.')