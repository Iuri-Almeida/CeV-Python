print("{:=^31}".format(" Exercício 034 "))

s = float(input("Qual o seu salário? R$"))

# if s > 1250:
#     print("O seu aumento foi de 10%, logo seu novo salário é R${:.2f}".format(s * 1.10))
# else:
#     print("O seu aumento foi de 15%, logo seu novo salário é R${:.2f}".format(s * 1.15))

print("O seu aumento foi de {}%, logo seu novo salário é R${:.2f}".format(10 if s > 1250 else 15, s * (1.10 if s > 1250 else 1.15)))
