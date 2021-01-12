from datetime import date
print("{:=^31}".format(" Exercício 039 "))

ano = int(input("Qual o seu ano de nascimento? "))
sexo = str(input("Qual o seu sexo? [M/F]")).strip().upper()

ano_atual = date.today().year

if sexo == "M":
    if (ano_atual - ano) > 18:
        print("Já passou {} anos do alistamento.".format((ano_atual - ano) - 18))
    elif (ano_atual - ano) < 18:
        print("Vc ainda vai se alistar daqui a {} anos.".format((18 - (ano_atual - ano))))
    else:
        print("Vc precisa se alistar esse ano!")
else:
    print("Vc não precisa se alistar!")
