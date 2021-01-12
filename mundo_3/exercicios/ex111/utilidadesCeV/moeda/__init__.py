def aumentar(p, v):
    return moeda(p * (1 + v / 100))


def diminuir(p, v):
    return moeda(p * (1 - v / 100))


def dobro(p):
    return moeda(p * 2)


def metade(p):
    return moeda(p / 2)


def moeda(v, m='R$'):
    return f'{m}{v:.2f}'.replace('.', ',')


def resumo(v, a, r):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(v):>10}')
    print(f'{"Dobro do preço:":<20}{dobro(v):>10}')
    print(f'{f"{a}% de aumento:":<20}{aumentar(v, a):>10}')
    print(f'{f"{r}% de redução:":<20}{diminuir(v, r):>10}')
    print('-' * 30)
