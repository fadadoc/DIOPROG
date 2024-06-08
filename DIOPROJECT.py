MENU = f'''
    DEPOSITAR = 1
    SACAR = 2
    VIZU = 3
    SAIR = 4
'''

LIMITE = 3

limite_comp = 0
banco = 0
while True:
    print(MENU)
    Escolha = int(input("Digito: "))
    if Escolha == 1:
        valor = int(input("VALOR: "))
        if limite_comp == LIMITE or valor > 500:
            print("ERROR!")
            continue
        banco += valor
        limite_comp += 1
    elif Escolha == 2:
        valor = int(input("VALOR: "))
        if limite_comp == LIMITE or valor > 500:
            print("ERROR!")
            continue
        banco -= valor
        limite_comp += 1
    elif Escolha == 3:
        print(banco)
    else:
        exit