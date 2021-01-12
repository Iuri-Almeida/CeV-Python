print("{:=^31}".format(" Exercício 024 "))

n = str(input("Digite o nome de uma cidade: ")).strip().capitalize()

print("A cidade começa com o nome 'Santo'? {}".format('Santo' in n.split()[0]))
