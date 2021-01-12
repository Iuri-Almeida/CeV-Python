def aumentar(p, v):
    return p * (1 + v / 100)


def diminuir(p, v):
    return p * (1 - v / 100)


def dobro(p):
    return p * 2


def metade(p):
    return p / 2


def moeda(v, m='R$'):
    return f'{m}{v:.2f}'.replace('.', ',')
