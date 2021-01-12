print("{:=^31}".format(" Exercício 051 "))

pt = int(input("Qual o primeiro termo da P.A.? "))
r = int(input("Qual a razão da P.A.? "))
print("-" * 25)
for i in range(10):
    print("O {}˚ termo da P.A. é: {}".format((i + 1), (pt + ((i + 1) - 1) * r)))
