# 7.	Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

def menores(num1, num2):
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    else:
        print(f"ambos os números são iguais")

ver1 = input ("Digite um número")
ver2 = input ("Digite mais um número")

menores(ver1, ver2)