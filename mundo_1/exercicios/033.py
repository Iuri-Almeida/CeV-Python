print("{:=^31}".format(" Exercício 033 "))

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

l = [n1, n2, n3]
l.sort()

print("O menor número é {} e o maior é {}.".format(l[0], l[2]))

# if n1 > n2:
#     if n1 > n3:
#         if n2 > n3:
#             print("O maior número é {} e o menor é {}.".format(n1, n3))
#         else:
#             print("O maior número é {} e o menor é {}.".format(n1, n2))
#     else:
#         print("O maior número é {} e o menor é {}.".format(n3, n2))
# else:
#     if n2 > n3:
#         if n1 > n3:
#             print("O maior número é {} e o menor é {}.".format(n2, n3))
#         else:
#             print("O maior número é {} e o menor é {}.".format(n2, n1))
#     else:
#         print("O maior número é {} e o menor é {}.".format(n3, n1))
