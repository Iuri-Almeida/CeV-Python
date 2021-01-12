print("{:=^31}".format(" Exercício 063 "))

n = int(input("Digite um número: "))
f1 = 0
f2 = i = 1
print("{} -> {} ->".format(f1, f2), end = " ")
while i <= (n - 2):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print("{} ->".format(f3), end = " ")
    i += 1
print("Fim!")