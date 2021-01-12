print("{:=^31}".format(" Exercício 049 "))

n = int(input("Digite um número para saber sua tabuada: "))
for i in range(1, 11):
    print("{:<2} x {:>2} = {:>2}".format(n, i, (i * n)))
