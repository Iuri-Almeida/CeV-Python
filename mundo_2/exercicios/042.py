print("{:=^31}".format(" Exercício 042 "))

r1 = int(input("Qual a medida do primeiro lado: "))
r2 = int(input("Qual a medida do segundo lado: "))
r3 = int(input("Qual a medida do terceiro lado: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print("Pode ser formado um triângulo e esse triângulo é equilátero!")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Pode ser formado um triângulo e esse triângulo é isósceles!")
    else:
        print("Pode ser formado um triângulo e esse triângulo é escaleno!")
else:
    print("Com as medidas {}, {} e {} não se pode formar um triângulo.".format(r1, r2, r3))
