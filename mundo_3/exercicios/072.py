ex = ' Exercício 072 '
print(f'{ex:=^31}')

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatroze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número de 0 à 20: '))
    while not 20 >= n >= 0:
        n = int(input('Tente novamente. Digite um número de 0 à 20: '))

    print(f'O número {n} por extenso é {extenso[n]}.')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Vc deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM')