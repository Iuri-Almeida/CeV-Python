from time import sleep
print("{:=^31}".format(" Exercício 059 "))

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
resp = 0
while resp != 5:
    print("--------- Menu ---------")
    print("|      {}[1]{} somar       |".format("\033[33m", "\033[m"))
    print("|      {}[2]{} multiplicar |".format("\033[33m", "\033[m"))
    print("|      {}[3]{} maior       |".format("\033[33m", "\033[m"))
    print("|      {}[4]{} novos n˚    |".format("\033[33m", "\033[m"))
    print("|      {}[5]{} sair        |".format("\033[33m", "\033[m"))
    print("------------------------")
    resp = int(input("=> "))

    while resp not in [1, 2, 3, 4, 5]:
        resp = int(input("Opção inválida! Tente novamente.\n=> "))

    if resp == 1:
        print("A soma de {:.2f} com {:.2f} é {:.2f}".format(n1, n2, (n1 + n2)))
    elif resp == 2:
        print("A multiplicação de {:.2f} com {:.2f} é {:.2f}".format(n1, n2, (n1 * n2)))
    elif resp == 3:
        print("O maior número entre {:.2f} e {:.2f} é {:.2f}".format(n1, n2, n1 if n1 > n2 else n2))
    elif resp == 4:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    elif resp == 5:
        print("Finalizando...")
    sleep(1)
print("Fim do programa!")
