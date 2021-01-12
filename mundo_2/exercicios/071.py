ex = ' Exercício 071 '
print(f'{ex:=^31}')

print('----- Caixa Eletrônico -----')
valor = int(input('Qual valor será sacado? R$'))
cinquenta = vinte = dez = um = 0
while valor >= 50:
    cinquenta += 1
    valor -= 50
while valor >= 20:
    vinte += 1
    valor -= 20
while valor >= 10:
    dez += 1
    valor -= 10
while valor >= 1:
    um += 1
    valor -= 1
print(f'Total de {cinquenta} cédulas de R$50.00')
print(f'Total de {vinte} cédulas de R$20.00')
print(f'Total de {dez} cédulas de R$10.00')
print(f'Total de {um} cédulas de R$1.00')