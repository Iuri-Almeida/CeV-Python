from math import sin, cos, tan, pi
print("{:=^29}".format(" Desafio 018 "))

a1 = float(input("Digite um ângulo: "))

a2 = a1 * (pi / 180)

print("O ângulo {:.2f}˚ tem seno = {:.2f}, cosseno = {:.2f} e tangente = {:.2f}".format(a1, sin(a2), cos(a2), tan(a2)))
