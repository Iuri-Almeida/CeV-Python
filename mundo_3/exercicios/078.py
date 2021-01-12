ex = ' Exercício 078 '
print(f'{ex:=^31}')

lista = []
for i in range(0, 5):
    lista.append(int(input(f'Digite o valor para a Posição {i}: ')))
maior = max(lista)
menor = min(lista)
posicao_maior = posicao_menor = ''
print(f'Vc digitou os valores: {lista}')
for j in range(len(lista)):
    if lista[j] == maior:
        posicao_maior += f'{j}... '
    elif lista[j] == menor:
        posicao_menor += f'{j}... '
print(f'O maior valor digitado foi {maior} e ele está na posição: {posicao_maior}')
print(f'O menor valor digitado foi {menor} e ele está na posição: {posicao_menor}')
