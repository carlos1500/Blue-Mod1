
trabalhadores = {}

perg = ["Digite o nome: ", "Digite o ano de nascimento: ", 
"Digite o ano de contrato: ", "Digite o salario: "]

ano = 2021
aposentadoria = 35

cont = True
while cont:

    lista = []
    for i in perg[0:2]:
        print(i)
        lista.append(input())
        if i == "Digite o ano de nascimento: ":
            idade = ano - int(lista [1])
            lista.append(idade)
                   
    print ("Digite o numero da Carteira de Trabalho: ")
    CT = int(input())
    if CT != 0:
        for i in perg[2:]:
            print(i)
            lista.append(input())

            if i == "Digite o ano de contrato: ":
                tempoTrab = ano - int(lista[3])   
                lista.append(tempoTrab)     
                tempoApos = aposentadoria - tempoTrab
                lista.append(tempoApos)

    trabalhadores [CT] = lista

    
    print("Didite 'S' para Sim e qualquer outra tecla para não: ")
    c = input().upper()
    if c == "S":
        cont = True
    else:
        cont = False  

for t in trabalhadores:
    
    if trabalhadores[t][4] > 35:
        print(f"{trabalhadores[t][0]} está aposentado.")
    else:
        print(f"{trabalhadores[t][0]} faltam {trabalhadores[t][5]} anos para se apposentar")


# 5. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

# pessoas = []
# mulheres = []
# idade_acimam = []
# flag = True
# soma_idade = 0

# while flag:
#     dados = {}
#     print()
#     nome = input("Digite o nome: ") 
#     while True:
#         sexo = input("Digite o sexo M/F: ").upper()
#         if sexo != "M" and sexo != "F":
#             print("Desculpe, entrada inválida, digite apenas M ou F: ")
#         else:
#             break
#     idade = int(input ("Digite a idade: "))
#     soma_idade += idade
    
#     dados ["nome"] = nome
#     dados ["sexo"] =  sexo
#     dados ["idade"] = idade

#     if sexo == "F":
#         mulheres.append(dados)  

#     pessoas.append(dados)
#     while True:
#         continuar = input("Deseja adicionar mais um? S/N: ").upper()
#         if continuar == "S":
#             break
#         elif continuar == "N":
#             flag = False
#             break
#         else:
#             print("Desculpe, entrada inválida, digite apenas S ou N: ")
    


# total = len(pessoas)
# media = soma_idade / total

# for i in pessoas:
#     if i["idade"] > media:
#         idade_acimam.append(i)


# print(f"cadastros: \n {pessoas}")
# print(f"foram cadastrados um total de {total} pessoas")
# print(f"A média da idade das pessoas cadastradas foi: {media} anos")
# print(f"As mulheres cadastradas foram: {mulheres}")
# print(f"As pessoas com idades acima da média foram: {idade_acimam}")


    


