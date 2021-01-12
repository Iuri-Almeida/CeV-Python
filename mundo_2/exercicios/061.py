print("{:=^31}".format(" Exercício 061 "))

pt = int(input("Primeiro termo da P.A.: "))
r = int(input("Razão da P.A.: "))
i = 1
while i <= 10:
    print("{} ->".format(pt + (i - 1) * r), end = " ")
    i += 1
print("Fim!")