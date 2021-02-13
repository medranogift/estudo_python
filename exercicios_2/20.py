def notas():

    nota1 = input("Coloque sua 1º nota: ")
    nota2 = input("Coloque sua 2º nota: ")
    nota3 = input("Coloque sua 3º nota: ")

    while nota1 == "" or nota2 == "" or nota3 == "" or len(nota1) > 3 or len(nota2) > 3 or len(nota3) > 3 :
        print ("Nota inválida")
        nota1 = input("Coloque sua 1º nota: ")
        nota2 = input("Coloque sua 2º nota: ")
        nota3 = input("Coloque sua 3º nota: ")
            
    media = (float(nota1) + float(nota2) + float(nota3)) / 3

    if media == 10:
        print ("Aprovado com Distinção")
    elif media >= 7:
        print ("Aprovado")
    elif media <7:
        print ("Reprovado")

    print("Sua média foi:",media)






notas()
print("Hellow world\nHello CMD")
