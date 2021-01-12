print(f'{" Exercício 103 ":=^31}')

def ficha(n = "<desconhecido>", g = 0):
    """
    -> Escreve uma frase com o nome do jogador e quantos gols ele fez.
    :param n: (opcional) O nome do jogador.
    :param g: (opcional) A quantidade de gols.
    :return: A frase formatada com o nome e quantidade de gols.
    """
    return f'O jogador {n} fez {g} gol(s) no campeonato.'

j = input('Nome do jogador: ')
gols = input('Número de gols: ')
gols = int(gols) if gols.isnumeric() else 0
if j.strip() == '':
    print(ficha(g = gols))
else:
    print(ficha(j, gols))
