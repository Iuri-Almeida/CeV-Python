print("{:=^31}".format(" Exercício 055 "))

maior = menor = 0
for i in range(1, 6):
    p = float(input("Qual o peso da {}˚ pessoa? ".format(i)))
    if i == 1:
        maior = menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print("O maior peso foi de {} kg e o menor foi de {} kg".format(maior, menor))