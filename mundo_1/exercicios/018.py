from math import sin, cos, tan, pi
print("{:=^31}".format(" Exercício 018 "))

a = float(input("Digite o ângulo que vc deseja: "))

rad = (a * pi) / 180
# math.randians()

sen = sin(rad)
cos = cos(rad)
tan = tan(rad)

print("O ângulo de {} tem o SENO de {:.2f}".format(a, sen))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(a, cos))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(a, tan))
