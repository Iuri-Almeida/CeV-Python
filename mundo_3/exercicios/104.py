print(f'{" Exercício 104 ":=^31}')

def leiaInt(x):
    """
    -> Lê somente valores inteiros.
    :param x: O valor a ser lido.
    :return: O valor lido.
    """
    b = input(x)
    while not b.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        b = input(x)
    return b


n = leiaInt('Digite um número: ')
print(f'Vc acabou de digitar o número {n}.')
