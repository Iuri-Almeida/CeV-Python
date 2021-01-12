ex = " Exercício 067 "
print(f'{ex:=^31}')

while True:
    n = int(input("Digite um número para saber sua tabuada: "))
    print('-' * 25)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i:>2} = {n * i}')
    print('-' * 25)
print('Fim')