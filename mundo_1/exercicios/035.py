print("{:=^31}".format(" Exercício 035 "))

r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print("É possível formar um triângulo com essas 3 retas! :)")
else:
    print("NÃO é possível formar um triângulo com essas 3 retas! :'(")
