from time import sleep
print(f'{" Exercício 098 ":=^31}')

def contador(i, f, p):
    p = 1 if (p == 0) else p
    p = -p if (p < 0) else p
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    p = -p if (i > f) else p
    f = (f - 1) if (p < 0) else (f + 1)
    for i in range(i, f, p):
        print(f'{i} ', end = '', flush = True)
        sleep(0.5)
    print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de persolnalizar a contagem!')
de = int(input(f'{"Início:":<7} '))
até = int(input(f'{"Fim:":<7} '))
passo = int(input(f'{"Passo:":<7} '))
contador(de, até, passo)
