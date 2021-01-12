from datetime import date
print("{:=^31}".format(" Exercício 054 "))

nam = am = 0
for i in range(7):
    ano = int(input("Em que ano a {}˚ pessoa nasceu? ".format(i + 1)))
    if (date.today().year - ano) >= 21:
        am += 1
    else:
        nam += 1
print("{} pessoas já atingiram a maioridade e {} ainda não.".format(am, nam))