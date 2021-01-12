from lib import menu, opc_0, opc_1, opc_2, opc_3
print(f'{" Exercício 115 ":=^31}')

# Programa Principal
while True:
    menu()
    opc = opc_0()
    if opc == '1':
        opc_1()
    elif opc == '2':
        opc_2()
    elif opc == '3':
        opc_3()
        break
