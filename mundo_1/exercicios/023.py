print("{:=^31}".format(" Exercício 023 "))

n = int(input("Digite um número de 0 a 9999: "))

print("Com o número {}, temos:\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(n, n % 10, (n % 100) // 10, (n % 1000) // 100, n // 1000))
