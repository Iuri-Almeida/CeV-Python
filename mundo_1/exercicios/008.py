print("{:=^31}".format(" Desafio 008 "))

n = float(input("Digite uma distância (em metros): "))

print("Em km: {:.3f}\nEm hm: {:.3f}\nEm dam: {:.3f}\nEm dm: {:.3f}\nEm cm: {:.3f}\nEm mm: {:.3f}".format((n / 1000), (n / 100), (n / 10), (n * 10), (n * 100), (n * 1000)))
