nome = input("Digite seu nome: ")
print("Prazer em te conhecer, {:-^20}!".format(nome))

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2

print("A soma é {}, a multiplicação é {} e a divisão é {:.3f}".format(s, m, d), end = ' >>> ')
print("A divisão inteira é {}, o resto da divisão é {} e a potência é {}".format(di, r, e))