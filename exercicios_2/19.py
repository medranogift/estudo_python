def matematica():
    pergunta = input("Coloque o numero: ")

    while len(pergunta) > 3 or pergunta == "":
        print("------------------\nNumero inválido\n------------------")
        pergunta = input("Coloque o numero: ")

    centena = pergunta[0]
    dezena = pergunta[1]
    unidade = pergunta[2]

    print(pergunta + " = " + centena + " centenas " + dezena + " dezenas " + unidade + " unidades")


matematica()













