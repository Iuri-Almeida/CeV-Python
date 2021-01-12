print("{:=^31}".format(" Exercício 027 "))

n = str(input("Digite um nome completo: ")).strip()

print("O primeiro nome é: {}".format(n.split()[0]))
print("O último nome é: {}".format(n.split()[-1]))
