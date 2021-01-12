print("{:=^31}".format(" Exercício 052 "))

n = int(input("Digite um número: "))
e = "é"
for i in range(2, n):
    if (n % i) == 0:
        e = "NÃO é"
        break
print("O número {} {} um número primo.".format(n, e))