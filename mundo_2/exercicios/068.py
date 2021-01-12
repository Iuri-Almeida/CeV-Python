from random import randint
from time import sleep
ex = " Exercício 068 "
print(f'{ex:=^31}')

tot = 0
while True:
    op = str(input("Vc quer PAR ou ÍMPAR? [P/I] ")).strip().upper()[0]
    n = int(input("Qual valor vc quer jogar? [0 - 10] "))
    while not 10 >= n >= 0:
        n = int(input("Digite um valor entre 0 e 10: "))
    print('Calculando...')
    comp = randint(0, 10)
    comp_str = 'P' if op == 'I' else 'I'
    sleep(1)
    print('-=-' * 10)
    print(f'Vc escolheu {op} e jogou {n}')
    print(f'Eu escolhi {comp_str} e joguei {comp}.')
    print('-=-' * 10)
    if ((n + comp) % 2) == 0:
        if op == 'P':
            tot += 1
            print('Parabéns! Vc venceu!\n')
        else:
            print('Vc perdeu!\n')
            break
    else:
        if op == 'I':
            tot += 1
            print('Parabéns! Vc venceu!\n')
        else:
            print('Vc perdeu!\n')
            break
print(f'Vc venceu {tot} vezes do computador.')