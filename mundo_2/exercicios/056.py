print("{:=^31}".format(" Exercício 056 "))
idades = maior_idade = mulheres_menos_vinte = 0
nome_mais_velho = ""
for i in range(1, 5):
    print("----- {}˚ pessoa -----".format(i))
    nome = str(input("Nome: ")).strip().title()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    idades += idade
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_menos_vinte += 1
media = idades / 4
print("\nA média das idades do grupo foi {:.2f}.".format(media))
print("O nome do homem mais velho é {} com {} anos.".format(nome_mais_velho, maior_idade))
print("O número de mulheres com menos de 20 anos é {}.".format(mulheres_menos_vinte))
