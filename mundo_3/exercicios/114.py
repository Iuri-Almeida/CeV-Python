import requests
print(f'{" Exercício 114 ":=^31}')

url = 'http://pudim.com.br/'
try:
    r = requests.get(url)
except Exception as erro:
    print(f'\033[31mNão foi possível acessar o site do Pudim.\033[m')
else:
    print('\033[33mConsegui acessar o site do Pudim com sucesso!\033[m')
finally:
    print('Obrigado, volte sempre!')
