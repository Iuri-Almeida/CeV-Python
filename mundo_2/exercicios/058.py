from random import randint
print("{:=^31}".format(" Exercício 058 "))

comp = randint(0, 10)
resp = int(input("Pensei em um número de 0 a 10, que número foi esse? "))
tent = 1
while comp != resp:
    m = "Menos" if resp > comp else "Mais"
    resp = int(input("{}... Tente de novo: ".format(m)))
    tent += 1
print("Parabéns, vc acertou com {} tentativas!".format(tent))