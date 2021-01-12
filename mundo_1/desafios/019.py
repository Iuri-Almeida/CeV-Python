import random
print("{:=^29}".format(" Desafio 019 "))

a1 = input("Qual o nome do aluno 01: ")
a2 = input("Qual o nome do aluno 02: ")
a3 = input("Qual o nome do aluno 03: ")
a4 = input("Qual o nome do aluno 04: ")

lista  = [a1, a2, a3, a4]

escolhido = random.choice(lista)

print("O aluno escolhido foi {}.".format(escolhido))
