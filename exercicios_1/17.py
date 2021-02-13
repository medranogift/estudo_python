print("--------------------------------------------------------------------------")
m2_tinta = input("Coloque quantos m² você quer pintar: ")

conta = (int(m2_tinta)/6) / 18
conta_galaomenor = (int(m2_tinta)/6) / 3.6

if conta > int(conta):
    print("--------------------------------------------------------------------------")
    print("Precisa de", int(conta)+1,"latas de tintas, que fica no valor de: R$",(int(conta)+1)*80)
elif conta_galaomenor
else:
    print("--------------------------------------------------------------------------")
    print("Precisa de", int(conta),"latas de tintas, que fica no valor de: R$",int(conta)*80)





#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 

#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados

#latas de 18 litros, que custam R$ 80,00 
#ou em galões de 3,6 litros, que custam R$ 25,00.

#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

#comprar apenas latas de 18 litros;

#comprar apenas galões de 3,6 litros;

#misturar latas e galões, de forma que o desperdício de tinta seja menor. 

#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.