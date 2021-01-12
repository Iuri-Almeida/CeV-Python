print("{:=^31}".format(" Exercício 062 "))

pt = int(input("Digite o primeiro termo da P.A.: "))
r = int(input("Digite a razão da P.A.: "))
i = n = 1
while n != 0:
    if i <= 10:
        print("{} ->".format(pt + (i - 1) * r), end = " ")
    else:
        n = int(input("\nQuantos número deseja ver após? "))
        for j in range(i, i + n):
            print("{} ->".format(pt + (j - 1) * r), end = " ")
        i = (i + n) - 1
    i += 1
print("Fim! Foram mostrados {} termos da P.A.".format(i - 1))