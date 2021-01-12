from datetime import date
print("{:=^31}".format(" Exercício 041 "))

a = int(input("Qual o ano de nascimento do atleta: "))

ano_atual = date.today().year

if (ano_atual - a) <= 9:
    print("Esse atleta tem {} anos e é da categoria mirim!".format((ano_atual - a)))
elif (ano_atual - a) <= 14:
    print("Esse atleta tem {} anos e é da categoria infantil!".format((ano_atual - a)))
elif (ano_atual - a) <= 19:
    print("Esse atleta tem {} anos e é da categoria junior!".format((ano_atual - a)))
elif (ano_atual - a) <= 25:
    print("Esse atleta tem {} anos e é da categoria sênior!".format((ano_atual - a)))
else:
    print("Esse atleta tem {} anos e é da categoria master!".format((ano_atual - a)))
