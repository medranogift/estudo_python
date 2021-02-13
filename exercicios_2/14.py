
def nota():

    nota1 = input("Coloque sua 1º nota: ")
    nota2 = input("Coloque sua 2 nota: ")

    while nota1 == "" or nota2 =="":
        print("Notas invalidas\n--------------------")
        nota1 = input("Coloque sua 1º nota: ")
        nota2 = input("Coloque sua 2 nota: ")

    media = (float(nota1) + float(nota2)) / 2

    if media < 4.0 :
        print("-------------------- \nSua média foi de:",media,"- Nota: E")
    elif media >= 4.0 and media < 5.9:
        print("-------------------- \nSua média foi de:",media,"- Nota: D")
    elif media >= 6.0 and media < 7.4:
        print("-------------------- \nSua média foi de:",media,"- Nota: C")
    elif media >= 7.5 and media < 8.9:
        print("-------------------- \nSua média foi de:",media,"- Nota: B")
    elif media >= 9.0 and media < 10.0:
        print("-------------------- \nSua média foi de:",media,"- Nota: A")

        

    
nota()


