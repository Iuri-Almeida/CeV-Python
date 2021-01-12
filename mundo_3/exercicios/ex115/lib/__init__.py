c = [
    '\033[m',       # 0 -> padrão
    '\033[31m',     # 1 -> texto vermelho
    '\033[32m',     # 2 -> texto verde
    '\033[33m',     # 3 -> texto amarelo
    '\033[34m'      # 4 -> texto azul
]


def linha(t):
    return '-' * t


def banner(txt, t):
    print(linha(t))
    print(txt.center(t))
    print(linha(t))


def texto(c1, txt):
    return f'{c[c1]}{txt}{c[0]}'


def opcoes(opcoes):
    for pos, op in enumerate(opcoes):
        print(f'{texto(3, pos + 1)} - {texto(4, op)}')


def menu():
    banner("MENU PRINCIPAL", 30)
    opcoes(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    print(linha(30))


def opc_0():
    opc = input(texto(2, "Sua opção > "))
    while opc not in '123':
        print(texto(1, 'ERRO! Digite uma opção válida!'))
        opc = input(texto(2, 'Sua opção > '))
    return opc


def opc_1():
    banner("PESSOAS CADASTRADAS", 30)
    while True:
        try:
            arq = open('cadastros.txt', 'rt')
        except:
            arq = open('cadastros.txt', 'x')
        else:
            pessoas = arq.readlines()
            if len(pessoas) == 0:
                print(texto(2, 'Ainda não temos nenhuma pessoa cadastrada.'))
            else:
                for p in pessoas:
                    p = p[:-1].split(',')
                    print(f'{p[0]:<20}{p[1]:>5} anos')
            break


def opc_2():
    banner("NOVO CADASTRO", 30)
    arq = open('cadastros.txt', 'at')
    nome = str(input('Nome: ')).strip().title()
    while True:
        try:
            idade = input('Idade: ').strip()
            idade = int(idade)
        except:
            print(texto(1, 'ERRO! Digite um número inteiro válido!'))
        else:
            print(f'{c[3]}Novo registro de {nome} adicionado!{c[0]}')
            break
    usuario = f'{nome},{idade}\n'
    arq.write(usuario)


def opc_3():
    print(texto(3, 'Até logo!'))
