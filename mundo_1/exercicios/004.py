print("======== Exercício 004 ========")

algo = input("Digite algo: ")

print("O tipo primitivo desse valor é {}".format(type(algo)))
print("Só contém espaços? {}".format(algo.isspace()))
print("É um número? {}".format(algo.isnumeric()))
print("É alfabético? {}".format(algo.isalpha()))
print("Está em letras maiúsculas? {}".format(algo.isupper()))
print("Está em letras minúsculas? {}".format(algo.islower()))
print("Está captalizada? {}".format(algo.istitle()))
