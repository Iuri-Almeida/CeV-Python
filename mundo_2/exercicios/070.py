ex = ' Exercício 070 '
print(f'{ex:=^31}')

total = mil = 0
produto = 1
while True:
    print(f'----- Produto {produto} -----')
    n = str(input('Produto: ')).strip().capitalize().split()
    n = ' '.join(n)
    p = float(input('Preço: R$'))
    if total == 0 or p < barato:
        barato = p
        nome = n
    if p > 1000:
        mil += 1
    total += p
    produto += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Vc deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'\nA) O total gasto na compra foi R${total:.2f}')
print(f'B) {mil} produtos custam mais de R$1000.00')
print(f'C) O produto mais barato é {nome} custando R${barato:.2f}')