print("{:=^31}".format(" Exercício 057 "))

s = str(input("Qual o seu sexo? [M/F] ")).strip().upper()[0]
while s not in "MF":
    s = str(input("Parece que ouve um erro de digitação, informa novamente seu sexo: [M/F] ")).strip().upper()[0]
print("O sexo escolhio foi {}.".format("masculino" if s == "M" else "feminino"))