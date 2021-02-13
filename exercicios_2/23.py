#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

def intordeci():
    
    numero = float(input("Coloque um numero: "))

    conta = round(numero)%numero


    if conta == 0:
        numeroconverint = int(numero)
        print(str(numeroconverint)+" é inteiro")
    else:
        print(str(numero)+" é decimal")

intordeci()