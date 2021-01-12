print("{:=^31}".format(" Exercício 031 "))

d = float(input("Qual a distância da viagem? "))

# if d <= 200:
#     print("O preço por esta viagem é de R${:.2f}.".format(d * 0.50))
# else:
#     print("O preço por esta viagem é de R${:.2f}.".format(d * 0.45))

print("O preço por esta viagem é de R${:.2f}.".format(d * (0.50 if d <= 200 else 0.45)))
