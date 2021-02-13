print ("Calculo de multa pesca")

kg_fish = input("Coloque quantos KG voce pescou aqui: ")

if int(kg_fish) <= 50:
    print("funfou")
else:
    print("Voce pescou",(int(kg_fish)-50),"KG a mais, a multa será de R$",(int(kg_fish)-50)*4)
