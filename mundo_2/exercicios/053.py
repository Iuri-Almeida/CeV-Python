print("{:=^31}".format(" Exercício 053 "))

f = str(input("Digite um frase: ")).strip().lower().split()
f = "".join(f)
e = "é" if f == f[::-1] else "NÃO é"
# e = "é"
# for i in range(len(f)):
#     if f[i] != f[- (i + 1)]:
#         e = "NÃO é"
#         break
print("A frase escrita {} um palíndromo.".format(e))