from math import factorial
print("{:=^31}".format(" Exercício 060 "))

n = int(input("Digite um número: "))
# i = n - 1
# while i >= 1:
#     n *= i
#     i -= 1
for i in range(n - 1, 0, -1):
    n *= i
print("O fatorial do número é {}.".format(1 if n == 0 else n))
