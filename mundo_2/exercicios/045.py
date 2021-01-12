from random import shuffle
from time import sleep

print("{:=^31}".format(" Exercício 045 "))

print("-=-" * 10)
print("{:^30}".format("Jokenpô"))
print("-=-" * 10)

print("\n----- Opção -----")
print("|   [1] pedra   |")
print("|   [2] papel   |")
print("|   [3] tesoura |")
print("-----------------")

op = int(input("=> "))

print("\nComputador jogando...", end = " ")
op_comp = ["pedra", "papel", "tesoura"]
shuffle(op_comp)
op_comp = op_comp[0]
sleep(2)
print(op_comp.upper())

if op == 1:
    if op_comp == "pedra":
        print("Empate!")
    elif op_comp == "papel":
        print("Vc perdeu!")
    else:
        print("Vc ganhou!")
elif op == 2:
    if op_comp == "pedra":
        print("Vc ganhou!")
    elif op_comp == "papel":
        print("Emapte!")
    else:
        print("Vc perdeu!")
else:
    if op_comp == "pedra":
        print("Vc perdeu!")
    elif op_comp == "papel":
        print("Vc ganhou!")
    else:
        print("Empate!")