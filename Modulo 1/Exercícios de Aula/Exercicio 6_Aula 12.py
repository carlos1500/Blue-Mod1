# 6. Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve 
# receber 5 notas de 15 alunos, assim como o nome desses alunos, o programa tem que
# calcular a média desse aluno e mostrar a situação dele, seguindo os mesmos critérios
# apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as
# situações dos 15 alunos de uma vez só.

total_alunos = int(input("Digite o total de alunos que deseja cadastrar: "))
lista_completa = []

for i in range(total_alunos):
    dados = {}
    nome = input("Digite o nome do estudante: ")
    nota_1 = float(input("Digite a nota de biologia: "))
    nota_2 = float(input("Digite a nota de matemática: "))
    nota_3 = float(input("Digite a nota de química: "))
    nota_4 = float(input("Digite a nota de física: "))
    nota_5 = float(input("Digite a nota de português: "))
    print()
    soma_notas = 0
    soma_notas += nota_1 
    soma_notas += nota_2
    soma_notas += nota_3
    soma_notas += nota_4 
    soma_notas += nota_5
    

    dados ["nome"] =  nome
    dados ["nota biologia"] =  nota_1
    dados ["nota matemática"] = nota_2
    dados ["nota química"] = nota_3
    dados ["nota física"] = nota_4
    dados ["nota português"] = nota_5
    media =  soma_notas / 5
    dados ["média final"] = media
    if media < 6:
        dados ["Status"] = "reprovado"
    elif media >= 6 and media < 7:
        dados ["Status"] = "Encaminhado à recuperação"
    elif media > 6.9:
        dados ["Status"] = "aprovado"

    lista_completa.append(dados)

print()
print(lista_completa)
print()

for a in lista_completa:
    print(f"Aluno: {a['nome']}, a média final foi {a['média final']}, o status de aprovação é {a['Status']}")



