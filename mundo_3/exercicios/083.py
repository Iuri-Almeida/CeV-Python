ex = ' Exercício 083 '
print(f'{ex:=^31}')

exp = str(input('Digite a expressão: ')).strip().lower()
for i in range(len(exp)):
    if exp.count('(') != exp.count(')') or exp[-1] == '(':
        print('Sua expressão está errada!')
        break
    elif (i + 1) < len(exp):
        if exp[i] == '(' and exp[i + 1] == ')':
            print('Sua expressão está errada!')
            break
    else:
        print('Sua expressão está correta!')
        break
