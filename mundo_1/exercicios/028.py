from random import randint
print("{:=^31}".format(" Exercício 028 "))

n = randint(0, 5)

resp = int(input("Qual o número que o computador pensou? "))

print("Vc acertou! :)" if resp == n else "Vc errou! :'(")
