from datetime import date
ex = ' Exercício 092 '
print(f'{ex:=^31}')

pessoa = {}
pessoa['Nome'] = str(input('Nome: ')).strip().capitalize()
ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
pessoa['Idade'] = ano_atual - ano
pessoa['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Ano de contratação'] + 35) - ano_atual)
print('-=-' * 14)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}.')
