def funcao():
    Numero1 = (input('Coloque o primeiro numero: '))
    Numero2 = (input('Coloque o segundo numero: '))
    Numero3 = (input('Coloque o terceiro numero: '))
    lista = [int(Numero1), int(Numero2), int(Numero3)]

    reverso = sorted(lista, reverse=True)

    print(reverso)

funcao()


#Faça um Programa que leia três números e mostre-os em ordem decrescente.

