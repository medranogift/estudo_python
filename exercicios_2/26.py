def posto_programa():
        
    litros = input("Coloque quantos litros gostaria: ")

    while litros == "":
        print("Litragem inválida")
        litros = input("Coloque quantos litros gostaria: ")

    combustivel = input("Coloque o tipo de combustivel [G/A]: ").upper()
    while combustivel != "G" and combustivel != "A":
        print("Combustivel inválido")
        combustivel = input("Coloque o tipo de combustivel [G/A]: ").upper()

    if combustivel == "G":
        if int(litros) <= 20:
            valor_litros = (int(litros) * 2.50)
            desconto4g = valor_litros * 0.04
            print("Os "+ litros +" litros de Gasolina ficaram: R$"+ str(valor_litros - desconto4g))
        if int(litros) > 20:  
            valor_litros = (int(litros) * 2.50)
            desconto6g = valor_litros * 0.06  
            print("Os "+ litros +" litros de Gasolina ficaram: R$"+ str(valor_litros - desconto6g))
    if combustivel == "A":
        if int(litros) <= 20:
            valor_litros = (int(litros) * 1.90)
            desconto3a = valor_litros * 0.03
            print("Os "+ litros +" litros de Álcool ficaram: R$"+ str(valor_litros - desconto3a))
        if int(litros) > 20:  
            valor_litros = (int(litros) * 1.90)
            desconto5a = valor_litros * 0.05  
            print("Os "+ litros +" litros de Álcool ficaram: R$"+ str(valor_litros - desconto5a))

posto_programa()
            

