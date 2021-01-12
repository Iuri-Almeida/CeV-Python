print("{:=^31}".format(" Exercício 048 "))

s = v = 0
for i in range(3, 501, 3):
    if (i % 2) == 1:
        v += 1
        s += i
print("A soma de {} valores foi {}.".format(v, s))
