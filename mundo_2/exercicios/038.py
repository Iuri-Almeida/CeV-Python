print("{:=^31}".format(" Exercício 038 "))

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("O {} é maior que {}.".format(n1, n2))
elif n1 < n2:
    print("O {} é maior que {}.".format(n2, n1))
else:
    print("Não existe valor maior, os dois são iguais.")
