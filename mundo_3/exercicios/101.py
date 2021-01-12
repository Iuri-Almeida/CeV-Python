print(f'{" Exercício 101 ":=^31}')

def voto(a):
    """
    -> Verifica a situação eleitoral da pessoa.
    :param a: Ano de nascimento da pessoa.
    :return: Frase dizendo qual a situação eleitoral.
    """
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - a
    frase = f'Com {idade} anos: VOTO '
    if idade < 16:
        frase += 'NEGADO!'
    elif idade < 18 or idade > 65:
        frase += 'OPCIONAL!'
    else:
        frase += 'OBRIGATÓRIO!'
    return frase
ano = int(input('Em que ano vc nasceu? '))
print(voto(ano))
