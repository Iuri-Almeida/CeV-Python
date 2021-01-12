from time import sleep
print("{:=^31}".format(" Exercício 043 "))

m = float(input("Qual é a sua massa corporal? "))
a = float(input("Qual é a sua altura? "))

imc = (m) / (a ** 2)

print("\nCom o imc = {:.2f}, vc está...".format(imc))
sleep(2)

if imc < 18.5:
    print("Abaixo do peso!")
elif imc < 25:
    print("Peso ideal!")
elif imc < 30:
    print("Sobrepeso!")
elif imc < 40:
    print("Obesidade!")
else:
    print("Obesidade mórbida!")
