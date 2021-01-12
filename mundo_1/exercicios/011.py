print("{:=^31}".format(" Exercício 011 "))

l = float(input("Qual a largura da parede? "))
a = float(input("Qual a altura da parede? "))

print("Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.3f}m².\nPara pintar essa parede, vc precisará de {:.4f}l de tinta.".format(l, a, l * a, (l * a) / 2))
