def conta():
    nota_1 = float(input("Coloque a nota do 1º Bimestre: "))
    nota_2 = float(input("Coloque a nota do 2º Bimestre: "))
    nota_3 = float(input("Coloque a nota do 3º Bimestre: "))
    nota_4 = float(input("Coloque a nota do 4º Bimestre: "))
    calculo_media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    
    print('Sua média foi de: ', calculo_media)

    if calculo_media == 10:
        print ('Aprovado com Distinção')
    elif calculo_media >= 7:
        print ('Aprovado')
    else:
        print ('Reprovado')


conta()


#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.