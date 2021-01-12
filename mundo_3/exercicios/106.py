from time import sleep
print(f'{" Exercício 106 ":=^31}')

cores = [
    '\033[m',       # 0 -> padrão
    '\033[30;41m',  # 1 -> fundo vermelho e letra branca
    '\033[31m',     # 2 -> letra vermelho
    '\033[7;30m',     # 3 -> fundo branco
    '\033[30;44m',  # 4 -> fundo azul e letra branca
    '\033[30;42m',  # 5 -> fundo verde e letra branca
]

def titulo(txt, cor = 0):
    """
    -> Escreve na tela títulos personalizados.
    :param txt: O texto que deseja escrever.
    :param cor: A cor que deseja colorir o texto.
    """
    tam = len(txt) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
    print(cores[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 5)
    r = input('Função ou biblioteca > ')
    while r == '':
        print(f'{cores[2]}ERRO! Busque por alguma coisa.{cores[0]}')
        r = input('Função ou biblioteca > ')
    if r.upper() == 'FIM':
        titulo('ATÉ LOGO!', 1)
        break
    titulo(f"Acessando o manual do comando '{r}'", 4)
    sleep(0.5)
    print(cores[3], end='')
    help(r)
    print(cores[0], end='')
    sleep(0.5)
