from time import sleep
print(f'{" Exercício 102 ":=^31}')

def fatorial(n, show = False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número que será calculado o fatorial.
    :param show: (opcional) Mostrar ou não a contagem.
    :return: O valor do fatorial do número n.
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            print(f'{i} {"=" if i == 1 else "x"}', end = ' ', flush = True)
            sleep(1)
    return f
print(fatorial(5, True))
help(fatorial)
