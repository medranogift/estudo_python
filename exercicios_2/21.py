def banco():

    saque = int(input("Quanto gostaria de sacar [10-600]? "))

    while saque > 600 or saque < 10:
        print("Valor inválido")
        saque = int(input("Quanto gostaria de sacar? "))

    cem = int(saque / 100)
    saque = saque - (cem * 100)

    cinquent = int(saque / 50)
    saque = saque - (cinquent * 50)

    dez  = int(saque / 10)
    saque = saque - (dez * 10)

    cinco  = int(saque / 10)
    saque = saque - (cinco * 10)


    um  = int(saque / 1)
    saque = saque - (um * 1)

    print('Notas R$100,00 = ',cem)
    print('Notas R$ 50,00 = ',cinquent)
    print('Notas R$ 10,00 = ',dez)
    print('Notas R$  5,00 = ',cinco)
    print('Notas R$  1,00 = ',um)

banco()

