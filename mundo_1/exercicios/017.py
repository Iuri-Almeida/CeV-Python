print("{:=^31}".format(" Exercício 017 "))

co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))

print("A hipotenusa vai medir {:.2f}.".format((co ** 2 + ca ** 2) ** (1/2)))
# from math import hypot
