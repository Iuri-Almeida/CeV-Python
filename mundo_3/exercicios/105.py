print(f'{" Exercício 105 ":=^31}')

def notas(* n, s = False):
    """
    -> Cria um dicionário com as notas recebidas.
    :param n: Uma ou mais notas dos alunos.
    :param s: (opcional) Mostrar ou não a situação dos alunos.
    :return: O dicionário com informações sobre as notas.
    """
    d = {}
    d['Total'] = len(n)
    d['Maior'] = max(n)
    d['Menor'] = min(n)
    d['Média'] = round((sum(n) / len(n)), 2)
    if s:
        if d['Média'] >= 7:
            d['Situação'] = 'Boa'
        elif d['Média'] >= 5:
            d['Situação'] = 'Razoável'
        else:
            d['Situação'] = 'Ruim'
    return d
r = notas(1, 4.5, 5, 6, 2.4, s = True)
print(r)
