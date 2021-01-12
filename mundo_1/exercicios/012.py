print("{:=^31}".format(" Exercício 012 "))

n = float(input("Qual é o preço do produto? R$"))

print("O produto que custava R${:.2f}, na promoção com desconto de 5%, vai custar R${:.2f}.".format(n, (n * 0.95)))
