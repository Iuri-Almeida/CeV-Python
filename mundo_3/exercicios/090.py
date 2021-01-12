ex = ' Exercício 090 '
print(f'{ex:=^31}')

aluno = {}
aluno['Nome'] = str(input('Nome: ')).strip().capitalize()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'aprovado'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'recuperação'
else:
    aluno['Situação'] = 'reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
