print("{:=^31}".format(" Exercício 022 "))

n = str(input("Digite um nome: ")).strip()

print("Letras maiúsculas: {}".format(n.upper()))
print("Letras minúsculas: {}".format(n.lower()))
print("Número de letras totais (sem espaço): {}".format(len("".join(n.split()))))
print("Número de letras do primeiro nome: {}".format(len(n.split()[0])))
