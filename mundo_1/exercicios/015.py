print("{:=^31}".format(" Exercício 015 "))

d = int(input("Quantos dias alugados? "))

km = float(input("Quantos quilômetros rodados? "))

print("O total a pagar é de R${:.2f}".format((60 * d) + (0.15 * km)))
