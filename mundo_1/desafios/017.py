from math import sqrt
print("{:=^29}".format(" Desafio 017 "))

cat1 = float(input("Digite o comprimento do cateto oposto: "))
cat2 = float(input("Digite o comprimento do cateto adjacente: "))

print("Com os catetos medindo {:.2f} e {:.2f}, temos uma hipotenusa que mede {:.2f}.".format(cat1, cat2, sqrt(cat1 ** 2 + cat2 ** 2)))
