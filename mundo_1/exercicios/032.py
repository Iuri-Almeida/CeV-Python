print("{:=^31}".format(" Exercício 032 "))

a = int(input("Digite um ano: "))

# if (a % 4) == 0 and (a % 100 != 0 or a % 400 == 0):
#     print("Esse é uma ano bissexto!")
# else:
#     print("Esse NÃO é um ano bissexto!")

print("Esse {} uma ano bissexto!".format("é" if (a % 4) == 0 and (a % 100 != 0 or a % 400 == 0)else "NÃO é"))
