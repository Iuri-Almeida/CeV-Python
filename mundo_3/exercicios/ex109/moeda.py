def aumentar(p, v, f=False):
    n = p * (1 + v / 100)
    return moeda(n) if f else n


def diminuir(p, v, f=False):
    n = p * (1 - v / 100)
    return moeda(n) if f else n


def dobro(p, f=False):
    n = p * 2
    return moeda(n) if f else n


def metade(p, f=False):
    n = p / 2
    return moeda(n) if f else n


def moeda(v, m='R$'):
    return f'{m}{v:.2f}'.replace('.', ',')
