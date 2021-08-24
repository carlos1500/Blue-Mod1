# 3.	 Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    custototal = custo * taxaImposto / 100 
    resultado = custo + custototal
    print (resultado)


valor = float(input("Digite o valor do seu produto "))
juros = float(input("Digite a taxa de juros "))

somaImposto(juros, valor)