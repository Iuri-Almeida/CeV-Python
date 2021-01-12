print("{:=^29}".format(" Desafio 011 "))

largura = float(input("Qual a largura da parede (em metros)? "))
altura = float(input("Qual a altura da parede (em metros)? "))

area = largura * altura

print("Vc precisará de {:.2f} litro(s) de tinta.".format(area / 2))
