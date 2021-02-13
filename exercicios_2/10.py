salario_base = float(input("Coloque o seu salário atual aqui: "))

def calculo_reajuste():

    calculo_20p = salario_base * 0.2
    calculo_15p = salario_base * 0.15
    calculo_10p = salario_base * 0.1
    calculo_5p = salario_base * 0.05
 
    if salario_base <= 280:
        print("---------------------------------------------------")
        print("Salário antes do reajuste: R$", salario_base)
        print("Percentual do aumento: 20%")
        print("Valor do aumento: R$", round(calculo_20p))
        print("O novo salário ficou de: R$", salario_base + calculo_20p)
        print("---------------------------------------------------")
    elif salario_base > 280 and salario_base <= 700:
        print("---------------------------------------------------")
        print("Salário antes do reajuste: R$", salario_base)
        print("Percentual do aumento: 15%")
        print("Valor do aumento: R$", round(calculo_15p))
        print("O novo salário ficou de: R$", salario_base + calculo_15p)
        print("---------------------------------------------------")
    elif salario_base > 700 and salario_base <= 1500:
        print("---------------------------------------------------")
        print("Salário antes do reajuste: R$", salario_base)
        print("Percentual do aumento: 10%")
        print("Valor do aumento: R$", round(calculo_10p))
        print("O novo salário ficou de: R$", salario_base + calculo_10p)
        print("---------------------------------------------------")
    elif salario_base > 1500:
        print("---------------------------------------------------")
        print("Salário antes do reajuste: R$", salario_base)
        print("Percentual do aumento: 5%")
        print("Valor do aumento: R$", round(calculo_5p))
        print("O novo salário ficou de: R$", salario_base + calculo_5p)
        print("---------------------------------------------------")

calculo_reajuste()