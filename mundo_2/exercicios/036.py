print("{:=^31}".format(" Exercício 036 "))

valor = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o salário do comprador? R$"))
anos = int(input("Em quantos anos vc vai pagar? "))

prestacao_mensal = valor / (anos * 12)

if prestacao_mensal <= (salario * 0.3):
    print("Parabéns! Seu empréstimo foi aprovado e tem uma prestação de R${:.2f}/mês e deve ser paga em {} anos.".format(prestacao_mensal, anos))
else:
    print("Empréstimo negado! A prestação de R${:.2f}/mês ultrapassou 30% do salário.".format(prestacao_mensal))
