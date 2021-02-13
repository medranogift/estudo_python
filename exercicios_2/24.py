def calculadora():
    num1 = input("Coloque o 1º numero: ")
    num2 = input("Coloque o 2º numero: ")

    while num1 == "" or num2 == "":
        print("Numeros inválidos")
        num1 = input("Coloque o 1º numero: ")
        num2 = input("Coloque o 2º numero: ")

    operacao = input("Operação a ser realizada [+ - / *]: ")
    while operacao != "+" and operacao != "-" and operacao != "/" and operacao != "*":
        print("Operação inválida")
        operacao = input("Operação a ser realizada [+ - / *]: ")

    print("----------------------------------------")
    if operacao == "+":
        resultado =  int(num1) + int(num2)
        print("O resultado é:", resultado)
    if operacao == "-":
        resultado =  int(num1) - int(num2)
        print("O resultado é:", resultado)
    if operacao == "/":
        resultado =  int(num1) / int(num2)
        print("O resultado é:", resultado)
    if operacao == "*":
        resultado =  int(num1) * int(num2)
        print("O resultado é:", resultado)


    parouimpar = resultado%2
    if parouimpar == 0:
        print("- É um numero par.")
    else:
        print("- É um umero impar.")

    if resultado >= 0:
        print("- É positivo.")
    else:
        print("- É negativo.")
    
    try:
        decimalornot = round(resultado)%resultado
        if decimalornot == 0:
            print("- É inteiro.")
        else:
            print("- É decimal.")
    except:
        print("- Neutro")

        print("----------------------------------------")

calculadora()
        