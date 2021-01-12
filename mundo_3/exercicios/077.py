ex = ' Exercício 077 '
print(f'{ex:=^31}')

tupla = (
    'arroz',
    'juliana',
    'carro',
    'mouse',
    'curso',
    'python',
    'chave',
    'urso',
    'aprender',
    'programar',
    'linguagem',
    'gratis',
    'estudar',
    'praticar',
    'trabalhar',
    'mercado',
    'programador',
    'futuro'
)
for i in tupla:
    print(f'\nNa palavra {i.upper()} temos as vogais: ', end = '')
    # for j in range(len(i)):
    #     if 'a' == i[j]:
    #         print('a ', end = '')
    #     elif 'e' == i[j]:
    #         print('e ', end = '')
    #     elif 'i' == i[j]:
    #         print('i ', end = '')
    #     elif 'o' == i[j]:
    #         print('o ', end = '')
    #     elif 'u' == i[j]:
    #         print('u ', end = '')
    for j in i.lower():
        if j in 'aeiou':
            print(j, end = ' ')
print('\nFim')
