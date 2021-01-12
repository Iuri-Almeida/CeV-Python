print("{:=^31}".format(" Exercício 064 "))

n = s = c = 0
while n != 999:
    n = int(input("Digite um número: "))
    if n != 999:
        s += n
        c += 1
print("Foram digitados {} número e a soma entre eles foi {}.".format(c, s))