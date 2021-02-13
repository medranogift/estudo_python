def acouge():

    tipocarne = input("Coloque o tipo de carne que deseja \n- File Duplo\n- Alcatra\n- Picanha\n>").lower()
    while tipocarne != "file duplo" and tipocarne != "alcatra" and tipocarne != "picanha":
        print("Tipo de carne inválido")
        tipocarne = input("Coloque o tipo de carne que deseja \n- File Duplo\n- Alcatra\n- Picanha\n>").lower()

    kgcarne = input("Quantos kg da carne gostaria?: ")
    formapag = input("Qual forma de pagamento gostaria de usar?\n1 - Cartao de Credito\n2 - Cartão Tabajara\n3 - Dinheiro\n>")
    while formapag != "1" and formapag != "2" and formapag != "3":
        print("Forma de pagamento inválida")
        formapag = input("Qual forma de pagamento gostaria de usar?\n1 - Cartao de Credito\n2 - Cartão Tabajara\n3 - Dinheiro\n>")

    if tipocarne == "file duplo":
        if int(kgcarne) <= 5:
            preco = int(kgcarne) * 4.9
            desc5 = 0
            if formapag == "2":
                desc5 = preco * 0.05
                preco = preco - desc5
        elif int(kgcarne) > 5:
            preco = int(kgcarne) * 5.8
            desc5 = 0
            if formapag == "2":
                desc5 = preco * 0.05
                preco = preco - desc5
    elif tipocarne == "alcatra":
        if int(kgcarne) <= 5:
            preco = int(kgcarne) * 5.9
            desc5 = 0
            if formapag == "2":
                desc5 = preco * 0.05
                preco = preco - desc5

        elif int(kgcarne) > 5:
            preco = int(kgcarne) * 6.8
            desc5 = 0
            if formapag == "2":
                desc5 = preco * 0.05
                preco = preco - desc5

    elif tipocarne == "picanha":
        if int(kgcarne) <= 5:
            preco = int(kgcarne) * 6.9
            desc5 = 0
            if formapag == "2":
                desc5 = preco * 0.05
                preco = preco - desc5

        elif int(kgcarne) > 5:
            preco = int(kgcarne) * 7.8
            desc5 = 0
            if formapag == "2":
                desc5 = preco * 0.05
                preco = preco - desc5

    print("Cupom Fiscal")
    tipocarnedic = {"picanha":"Picanha" }
    print("Produto - "+tipocarnedic["picanha"])
    print("Preço total: R$", preco - desc5)

    pagamentodic = {"1":"Cartao de Crédito","2":"Cartão Tabajara","3":"Dinheiro"}
    print("Tipo de pagamento: "+ pagamentodic[formapag])

    if desc5 != 0:
        print("Valor do desconto: R$", float(desc5))
    else:
        print("Sem desconto")

    print("Valor a pagar: R$", float(preco))

acouge()