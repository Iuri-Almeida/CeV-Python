print("{:=^31}".format(" Exercício 026 "))

n = str(input("Digite uma frase: ")).strip().lower()

print("A letra 'a' aparece {} vezes na frase.".format(n.count('a')))
print("A letra 'a' aparece na posição {} pela primeira vez.".format(n.find('a') + 1))
print("A letra 'a' aparece na posição {} pela última vez.".format(n.rfind('a') + 1))
