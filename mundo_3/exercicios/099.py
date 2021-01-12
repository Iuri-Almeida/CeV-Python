from time import sleep
print(f'{" Exercício 099 ":=^31}')

def maior(* num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end = ' ', flush = True)
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    maior = max(num) if len(num) > 0 else 0
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
