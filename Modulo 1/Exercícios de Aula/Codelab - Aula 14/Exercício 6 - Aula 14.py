# 6.	Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).


# Nota	Conceito
# >=9.0	A
# >=8.0	B
# >=7.0	C
# >=6.0	D
# <=4.0	F


def notas(nota):
    if nota >= 9:
        nota = 'A'
    elif nota >= 8:
        nota = 'B'
    elif nota >= 7:
        nota = 'C'
    elif nota >= 6:
        nota = 'D'
    elif nota <= 4:
        nota = 'F'

    print(nota)    

n = float(input("Digite a nota numerica: "))

