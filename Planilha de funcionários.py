import pandas as pd

### O objetivo desse programa é ajudar o financeiro a cálcular o valor dos sálarios ###
### de cada funcionário, levando em conta um valor fixo para a base salárial única  ###

nomes = []    #Lista pra os nomes dos funcionários
idades = []   #Lista para a idade dos funcionários
horas = []    #Lista para as horas trabalhadas dos funcionários
salarios = [] #Lista para os salário dos funcionários

#Essa classe serve para definir os dados e parametros que iremos usar
class rh:

    #Essa função tem o proposito de adicionar os dados principais dos funcionários para as listas definidas anteriormente
    def dados():

        #n é o numero de funcionários que você quer adicionar na planilha
        n = int(input("Quantos funcionários você têm?:  "))

        #i é uma variavel que usamos para dar um valor inicial a contagem de funcionários
        i = 1

        #Nesse loop você irá adicionar os 3 principais dados dos funionários
        while i <= n:
            nome = input("Nome:  ")
            nomes.append(nome)
            idade = int(input("Idade:  "))
            idades.append(idade)
            hora = int(input("Horas trabalhadas:  "))
            horas.append(hora)
            print("""
                    ======================
                    """)
            i = i + 1
        print("""


        """)

    #Essa função tem o objetivo de cálcular o sálario de cada funcionário
    def salarios():

        #A base é um valor fixo e unico para calcular o sálario
        base = int(input("Qual é o valor base para o cálculo do salário:  "))
        for i in horas:

            #O calculo do sálario é feito pela base vezes o numero de horas trabalhadas
            n = i * base
            salarios.append(n)

        print("""


        """)

    #Essa função tem o objetivo de deixar os dados organizados e separados em uma data frame e prontos para a visualização
    def planilha():
        Planilha = {}
        Planilha["Nomes"] = nomes
        Planilha["Idades"] = idades
        Planilha["Horas"] = horas
        Planilha["Salário"] = salarios

        dataFrame = pd.DataFrame(Planilha)
        print(dataFrame)

        print("""


        """)
        
        dataFrame.to_csv("Planilha dos funcionários", encoding='utf-8', index=False)

#aqui estamos chamando as funções e garantindo que quando abra o aplicativo tudo esteja pronta para começar
rh.dados()
rh.salarios()
rh.planilha()

