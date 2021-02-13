#Faça um Programa que pergunte em que turno você estuda. 
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!"

nome = input('Qual seu nome jovem? ')
pergunta_turno = input("Coloque o turno que voce estuda (M = Matutino, V = Vespertino ou N = Noturno): ")
bomdia = ["M", "m"]
boatarde = ["V", "v"]
boanoite = ["N", "n"]

def funcao():
    if pergunta_turno == "":
        print("Valor inválido")
    elif pergunta_turno in bomdia: #M
        print ("Bom dia, ", nome)
    elif pergunta_turno in boatarde: #V
        print ("Boa tarde, ", nome)
    elif pergunta_turno in boanoite: #N
        print ("Boa Noite, ",nome)
    else:
        print("Valor inválido")
funcao()