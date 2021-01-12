ex = ' Exercício 089 '
print(f'{ex:=^31}')

alunos = []
num = 1
while True:
    print(f'----- {num}˚ Aluno -----')
    aluno = []
    notas = []
    aluno.append(str(input('Nome: ')).strip().capitalize())
    notas.append(float(input('Nota 01: ')))
    notas.append(float(input('Nota 02: ')))
    aluno.append(notas[:])
    alunos.append(aluno[:])
    num += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 14)
print('{:<3} {:<10} {:<5}'.format('N˚', 'NOME', 'MÉDIA'))
print('-' * 30)
for pos, pessoa in enumerate(alunos):
    media = sum(pessoa[1]) / len(pessoa[1])
    print('{:<3} {:<10} {:<5.1f}'.format(pos, pessoa[0], media))
print('-' * 30)
while True:
    opc = int(input('Deseja ver a nota de que aluno? (999 interrompe): '))
    if opc == 999:
        break
    while opc >= len(alunos):
        opc = int(input('Tente novamente. Deseja ver a nota de que aluno? (999 interrompe): '))
    print(f'As notas de {alunos[opc][0]} são: {alunos[opc][1]}')
print('Fim')
