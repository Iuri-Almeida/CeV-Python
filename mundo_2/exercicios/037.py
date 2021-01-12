print("{:=^31}".format(" Exercício 037 "))

n = int(input("Digite um número: "))

print("\n------ Opção ------")
print("|   [1] Binário   |")
print("|   [2] Octal     |")
print("|   [3] Hexa      |")
print("-------------------")

resp = int(input("=> "))

if resp == 1:
    # binario
    print("\nO binário do número {} é {}.".format(n, bin(n)[2:]))
elif resp == 2:
    # octal
    print("\nO octal do número {} é {}.".format(n, oct(n)[2:]))
elif resp == 3:
    # hexa
    print("\nO hexadecimal do número {} é {}.".format(n, hex(n)[2:].upper()))
else:
    print("Opção inválida! Tente novamente!")