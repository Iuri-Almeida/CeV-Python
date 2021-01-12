print("{:=^31}".format(" Exercício 044 "))

preco = float(input("Informe o preço do produto: R$"))

print("\n----- Formas de pagamento -----")
print("| [1] à vista dinheiro/cheque |")
print("| [2] à vista cartão          |")
print("| [3] 2x no cartão            |")
print("| [4] 3x ou mais no cartão    |")
print("-------------------------------")

tipo_pag = int(input("Informe o tipo de pagamento: "))

if tipo_pag == 1:
    print("Receba 10% de desconto e pague R${:.2f}".format(preco * 0.9))
elif tipo_pag == 2:
    print("Receba 5% de desconto e pague R${:.2f}".format(preco * 0.95))
elif tipo_pag == 3:
    print("Pague o preço normal do produto, R${:.2f}".format(preco))
elif tipo_pag == 4:
    vezes = int(input("Quantas vezes deseja parcelar? "))
    print("Receba 20% de juros e pague R${:.2f}/parcela".format((preco / vezes) * 1.2))
else:
    print("Erro na escolha do pagamento!")
