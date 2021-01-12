from random import shuffle
print("{:=^31}".format(" Exercício 020 "))

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

l = [a1, a2, a3, a4]

shuffle(l)

print("A ordem da apresentação será:\n1˚: {}\n2˚: {}\n3˚: {}\n4˚: {}".format(l[0], l[1], l[2], l[3]))
