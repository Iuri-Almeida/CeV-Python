ex = " Exercício 066 "
print(f'{ex:=^31}')

s = c = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram digitados {c} número e a soma foi {s}.')
