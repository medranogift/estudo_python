def checkname():
    nome = input("Coloque seu nome: ")
    nomecontador = len(nome)
    while nomecontador < 5:
        print("Nome inválido")
        nome = input("Coloque seu nome: ")
        nomecontador = len(nome)
   
    idade = int(input("Coloque sua idade: "))
    while idade < 0 or idade > 150:       
        print("Idade inválida ")
        idade = int(input("Coloque sua idade: "))
   
    salario = int(input("Coloque o seu sálario: "))
    while salario < 0:
        print("Salário Inválido") 
        salario = int(input("Coloque o seu sálario: "))

    sexo = input("Coloque seu genero [M/F]: ").upper()
    while sexo != "M" and sexo != "F":
        print("Genero inválido")
        sexo = input("Coloque seu genero [M/F]: ").upper()
    
    estadocivil = input("Coloque seu estado civil [S/C/V/D]: ").upper()
    while estadocivil != "S" and estadocivil != "C" and estadocivil != "V" and estadocivil != "D":
        print("Estado civil inválido")
        estadocivil = input("Coloque seu estado civil [S/C/V/D]: ").upper()

    print("----------------------------------")
    print(nome)
    print(idade,"anos")
    print("Sálario de: R$", salario)
    Dici_sexo = {"M":"Masculino","F":"Feminino"}
    print(Dici_sexo[sexo])
    Dici_civil ={"S":"Solteiro","C":"Casado","V":"Viuvo","D":"Dicionario"}
    print(Dici_civil[estadocivil])
    print("----------------------------------")

checkname()

