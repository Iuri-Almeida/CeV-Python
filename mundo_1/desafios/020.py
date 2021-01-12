import random
print("{:=^29}".format(" Desafio 020 "))

a1 = input("Digite o nome do aluno 01: ")
a2 = input("Digite o nome do aluno 02: ")
a3 = input("Digite o nome do aluno 03: ")
a4 = input("Digite o nome do aluno 04: ")

lista = [a1, a2, a3, a4]

random.shuffle(lista)

print("A ordem de apresentação foi: 1˚: {}, 2˚: {}, 3˚: {}, 4˚: {}".format(lista[0], lista[1], lista[2], lista[3]))
