print("{:=^31}".format(" Exercício 050 "))

s = 0
for i in range(1, 7):
    n = int(input("Digite o {}˚ número: ".format(i)))
    s += n if (n % 2) == 0 else 0
print("A soma total de números pares foi {}.".format(s))
