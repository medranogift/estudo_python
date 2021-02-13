
from datetime import datetime

def Programa_horas():  

    hora_inicial = input("Coloque a hora inicial, Ex:[00:00:00]: ")
    hora_final = input("Coloque a hora final, Ex:[00:00:00]: ")
    #---------------------------------------------
    Lista_horainicial = hora_inicial.split(":")
    valor1_inicial = Lista_horainicial[0]
    valor2_inicial = Lista_horainicial[1]
    valor3_inicial = Lista_horainicial[2]

    Lista_horafinal = hora_final.split(":")
    valor1_final = Lista_horafinal[0]
    valor2_final = Lista_horafinal[1]
    valor3_final = Lista_horafinal[2]
    #---------------------------------------------
    hora1_I = valor1_inicial
    hora2_I = valor2_inicial    
    hora3_I = valor3_inicial
    juntarhoras_inicial = hora1_I + ":" + hora2_I + ":" + hora3_I

    hora1_F = valor1_final
    hora2_F = valor2_final
    hora3_F = valor3_final
    juntarhoras_final = hora1_F + ":" + hora2_F + ":" + hora3_F
    #---------------------------------------------
    d1 = datetime.strptime(juntarhoras_inicial, "%H:%M:%S")
    d2 = datetime.strptime(juntarhoras_final , "%H:%M:%S")

    subtracao = d1-d2

    print("O tempo entre os 2 horários é de: ", subtracao)

Programa_horas()



'''from datetime import datetime
s1 = '10:03:11'
s2 = '11:03:11' # for 1example
format = '%H:%M:%S'
time = datetime.strptime(s2, format) - datetime.strptime(s1, format)
print (time)'''
