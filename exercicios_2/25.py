def policiateste():
    pergunta1 = input("Telefonou para a vítima? " ).upper()
    print("-----------------------------")  
    while pergunta1 != "SIM" and pergunta1 != "NAO":
        print("- Inválido, coloque [SIM/NAO]")
        pergunta1 = input("Telefonou para a vítima? " ).upper()
        print("-----------------------------")  
    print("-----------------------------")      
    pergunta2 = input("Esteve no local do crime? " ).upper()
    while pergunta2 != "SIM" and pergunta2 != "NAO":
        print("- Inválido, coloque [SIM/NAO]")
        pergunta2 = input("Esteve no local do crime? " ).upper()
        print("-----------------------------")  
    print("-----------------------------") 
    pergunta3 = input("Mora perto da vítima? " ).upper()
    while pergunta3 != "SIM" and pergunta3 != "NAO":
        print("- Inválido, coloque [SIM/NAO]")
        pergunta3 = input("Mora perto da vítima? " ).upper()
        print("-----------------------------")  
    print("-----------------------------") 
    pergunta4 = input("Devia para a vítima? " ).upper()
    while pergunta4 != "SIM" and pergunta4 != "NAO":
        print("- Inválido, coloque [SIM/NAO]")
        pergunta4 = input("Devia para a vítima? " ).upper()
        print("-----------------------------")  
    print("-----------------------------") 
    pergunta5 = input("Já trabalhou com a vítima? " ).upper()
    while pergunta5 != "SIM" and pergunta5 != "NAO":
        print("- Inválido, coloque [SIM/NAO]")
        pergunta5 = input("Já trabalhou com a vítima? " ).upper()
        print("-----------------------------")  
    print("-----------------------------") 
    if pergunta1 == "SIM":
        p1 = 1
    elif pergunta1 == "NAO":
        p1 = 0

    if pergunta2 == "SIM":
        p2 = 1
    elif pergunta2 == "NAO":
        p2 = 0

    if pergunta3 == "SIM":
        p3 = 1
    elif pergunta3 == "NAO":
        p3 = 0

    if pergunta4 == "SIM":
        p4 = 1
    elif pergunta4 == "NAO":
        p4 = 0

    if pergunta5 == "SIM":
        p5 = 1
    elif pergunta5 == "NAO":
        p5 = 0

    conta = p1 + p2 + p3 + p4 + p5

    if conta < 2:
        print("- Inocente")
    elif conta == 2:
        print("- Suspeito(a)")
    elif conta >= 3 and conta <= 4:
        print("- Cumplice")
    elif conta == 5:
        print("- Assasino")

policiateste()
