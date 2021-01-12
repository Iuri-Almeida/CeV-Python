print("{:=^31}".format(" Exercício 029 "))

v = float(input("Qual a velocidade do carro? "))

if v > 80:
    print("Vc foi multado e terá que pagar R${:.2f}.".format((v - 80) * 7))
else:
    print("Tudo certo!")
