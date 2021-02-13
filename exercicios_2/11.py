salario_bruto = float(input("Coloque o quando você ganha por mes: "))

def programa_calculo():

    #IR alteravel por salario
    IR_ate1500 = salario_bruto * 0.05
    IR_ate2500 = salario_bruto * 0.1
    IR_mais2500 = salario_bruto * 0.2

    #Sindicato
    sindicato = salario_bruto * 0.03

    #FGTS 11% todos
    FGTS = salario_bruto * 0.11

    #INSS 10% todos
    INSS= salario_bruto * 0.1

    if salario_bruto <= 900:
        print ("-------------------------------------------")
        print ("  Salário Bruto: (5 * 220) : R$", salario_bruto )
        print ("  (-) IR (Isento)          : R$ 0,00"  )
        print ("  (-) INSS (10%)           : R$", INSS )
        print ("  FGTS (11%)               : R$", FGTS )
        print ("  Total de descontos       : R$", INSS + sindicato )
        print ("  Salário Liquido          : R$", salario_bruto - (INSS + sindicato) )
        print ("-------------------------------------------")
    elif salario_bruto > 900 and salario_bruto <= 1500:
        print ("-------------------------------------------")
        print ("  Salário Bruto: (5 * 220) : R$", salario_bruto )
        print ("  (-) IR (5%)              : R$", IR_ate1500 )
        print ("  (-) INSS (10%)           : R$", INSS )
        print ("  FGTS (11%)               : R$", FGTS )
        print ("  Total de descontos       : R$", IR_ate1500 + INSS + sindicato )
        print ("  Salário Liquido          : R$", salario_bruto - (IR_ate1500 + INSS + sindicato) )
        print ("-------------------------------------------")
    elif salario_bruto > 1500 and salario_bruto <= 2500:
        print ("-------------------------------------------")
        print ("  Salário Bruto: (5 * 220) : R$", salario_bruto )
        print ("  (-) IR (10%)             : R$", IR_ate2500 )
        print ("  (-) INSS (10%)           : R$", INSS )
        print ("  FGTS (11%)               : R$", FGTS )
        print ("  Total de descontos       : R$", IR_ate2500 + INSS + sindicato )
        print ("  Salário Liquido          : R$", salario_bruto - (IR_ate2500 + INSS + sindicato) )
        print ("-------------------------------------------")
    elif salario_bruto > 2500:
        print ("-------------------------------------------")
        print ("  Salário Bruto: (5 * 220) : R$", salario_bruto )
        print ("  (-) IR (20%)             : R$", IR_mais2500 )
        print ("  (-) INSS (10%)           : R$", INSS )
        print ("  FGTS (11%)               : R$", FGTS )
        print ("  Total de descontos       : R$", IR_mais2500 + INSS + sindicato )
        print ("  Salário Liquido          : R$", salario_bruto - (IR_mais2500 + INSS + sindicato) )
        print ("-------------------------------------------")


programa_calculo()