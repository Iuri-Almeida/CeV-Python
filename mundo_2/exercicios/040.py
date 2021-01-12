from time import sleep
print("{:=^31}".format(" Exercício 040 "))

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))

m = (n1 + n2) / 2

print("Com a média {:.1f} vc está...".format(m))
sleep(2)
if m < 5:
    print("REPROVADO!")
elif m <= 6.9:
    print("RECUPERAÇÃO!")
else:
    print("APROVADO!")
