print('Calculo de quanto você ganha por mês')
MoneyperHour = input("Coloque quanto você ganha por hora: ")
Timeperday = input("Coloque quantas horas você trabalha por dia: ")

conta = float(MoneyperHour)* int(Timeperday) * 30

print("Você ganha R$",int(conta),"por mês")
