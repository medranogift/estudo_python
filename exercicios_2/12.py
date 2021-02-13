valor = int(input("Digite um numero de 1 a 7: "))

def dias_semana():
    if (valor) == 1:
        print ("1-Domingo")
    elif valor == 2:
        print ("2-Segunda-Feira")
    elif valor == 3:
        print ("3-Terça-Feira")
    elif valor == 4:
        print ("4-Quarta-Feira")
    elif valor == 5:
        print ("5-Quinta-Feira")
    elif valor == 6:
        print ("6-Sexta-Feira")
    elif valor == 7:
        print ("7-Sábado")
    else:
        print ("Valor inválido")

dias_semana()