ex = ' Exercício 080 '
print(f'{ex:=^31}')

lista = []
# for i in range(5):
#     n = int(input('Digite um número: '))
#     if lista == []:
#         print('Adicionado ao final da lista...')
#         lista.append(n)
#     else:
#         for j in range(len(lista)):
#             if (j + 1) < len(lista):
#                 if n >= lista[j] and n <= lista[j + 1]:
#                     print(f'Adicionado na posição {j + 1} da lista...')
#                     lista.insert((j + 1), n)
#                     break
#                 elif n < lista[j]:
#                     print(f'Adicionado na posição {j} da lista...')
#                     lista.insert(j, n)
#                     break
#             else:
#                 if n >= lista[j]:
#                     print('Adicionado ao final da lista...')
#                     lista.append(n)
#                     break
#                 else:
#                     print(f'Adicionado na posição {j} da lista...')
#                     lista.insert(j, n)
#                     break
for i in range(5):
    n = int(input('Digite um valor: '))
    if i == 0 or n >= lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        for pos, j in enumerate(lista):
            if n <= j:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
print('-=-' * 10)
print(f'A lista ordenada é: {lista}')
