print(f'{" Exercício 113 ":=^31}')


def leia_int(x):
    """
    -> Lê somente valores inteiros.
    :param x: O valor a ser lido.
    :return: O valor lido.
    """
    while True:
        try:
            b = int(input(x))
        except (ValueError, TypeError):
            print('\033[31mErro na digitação do valor. Só aceitamos valores inteiros.\033[m')
        except KeyboardInterrupt:
            print('\033[31m\nO usuário preferiu não informar o valor.\033[m')
            return 0
        else:
            return b


def leia_float(x):
    """
    -> Lê somente valores do tipo float.
    :param x: O valor a ser lido.
    :return: O valor lido.
    """
    while True:
        try:
            b = float(input(x))
        except (ValueError, TypeError):
            print('\033[31mErro na digitação do valor. Só acietamos valores do tipo float.\033[m')
        except KeyboardInterrupt:
            print('\033[31m\nO usuário preferiu não informar o valor.\033[m')
            return 0
        else:
            return b


i = leia_int('Digite um número Inteiro: ')
r = leia_float('Digite um número Real: ')
print(f'Vc acabou de digitar o valor inteiro {i} e o valor real {r}.')
