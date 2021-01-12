ex = ' Exercício 081 '
print(f'{ex:=^31}')

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
if 5 in lista:
    valor_5 = "foi"
    posicao_5 = f' e está na posição {lista.index(5)} da lista'
else:
    valor_5 = "NÃO foi"
    posicao_5 = ''
lista.sort(reverse = True)
print(f'\nA) O total de números digitados foi de {len(lista)}.')
print(f'B) A lista em ordem decrescente é: {lista}.')
print(f'C) O valor 5 {valor_5} digitado{posicao_5}.')