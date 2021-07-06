def area(l1,l2):
    resultado = l1 * l2
    print(f"a área do seu retângulo é: {resultado}")


calculo = print("Insira o cumprimento dos lados do seu retângulo")
lado1 = int(input("Digite o primeiro lado "))
lado2 = int(input("Digite o segundo lado "))

resultado = area(lado1, lado2)
print(resultado)