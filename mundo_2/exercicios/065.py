print("{:=^31}".format(" Exercício 065 "))

resp = "S"
maior = menor = soma = total = 0
while resp == "S":
    n = int(input("Digite um número: "))
    soma += n
    total += 1
    if total == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
media = soma / total
print("A média entre {} valores digitados foi {}, o maior valor foi {} e o menor foi {}.".format(total, media, maior, menor))