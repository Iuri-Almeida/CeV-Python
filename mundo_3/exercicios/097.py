print(f'{" Exercício 097 ":=^31}')

def escreva(txt):
    txt = f'  {txt}  '
    t = len(txt)
    print('~' * t)
    print(f'{txt}')
    print('~' * t)


txt = str(input('Digite uma frase: '))
escreva(txt)
