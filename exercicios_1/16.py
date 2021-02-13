print("--------------------------------------------------------------------------")
m2_tinta = input("Coloque quantos m² você quer pintar: ")

conta = (int(m2_tinta)/3) / 18

if conta > int(conta):
    print("--------------------------------------------------------------------------")
    print("Precisa de", int(conta)+1,"latas de tintas, que fica no valor de: R$",(int(conta)+1)*80)
else:
    print("--------------------------------------------------------------------------")
    print("Precisa de", int(conta),"latas de tintas, que fica no valor de: R$",int(conta)*80)


#elif conta <= int(conta):
    #print("Precisa de", int(conta))
