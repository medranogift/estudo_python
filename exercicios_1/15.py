Money_Hour = input("Coloque quanto você ganha por hora: ")
Time_Work = input ("Coloque quantas horas você trabalha por dia: ")

salario_mes = (float(Money_Hour) * int(Time_Work))*30

IR = (salario_mes * 0.11)
INSS= (salario_mes * 0.08)
Sindi= (salario_mes * 0.05)
Somaimpostos= IR + INSS +Sindi

salario_liquido = (salario_mes) - Somaimpostos

print ("Resultado:")
print ("+ Salário Bruto : R$", salario_mes)
print ("- IR (11%) : R$", IR)
print ("- INSS (8%) : R$", INSS)
print ("- Sindicato ( 5%) : R$", Sindi)
print ("= Salário Liquido : R$", salario_liquido)

