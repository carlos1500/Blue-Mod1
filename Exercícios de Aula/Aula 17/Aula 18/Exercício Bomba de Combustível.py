#a. Crie uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i. tipoCombustivel.
# ii. valorLitro.
# iii. quantidadeCombustivel.
# b. A classe deve possuir no mínimo esses métodos:
# i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que
# foi colocada no veículo.
# ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor
# a ser pago pelo cliente.
# iii. alterarValor( ) – altera o valor do litro do combustível.
# iv. alterarCombustivel( ) – altera o tipo do combustível.
# v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.


class BombaCombustivel:
    def __innit__(self, tipocombustível, quantidadecombustível):
        self.tipocombustível = tipocombustível
        self.valorlitro = 0
        self.quantidadecombustível = quantidadecombustível

        def abastecerporvalor():
            valor = float(input("Digite o valor que deseja abastecer: "))
            total = valor / self.valorlitro
            return total

        def abastecerporlitro():
            total = float(input("Digite quantos litros deseja abastecer: "))
            totalapagar = total * self.valorlitro
            return totalapagar

        def alterarvalor():
            change = float(input("Digite o novo valor do litro: "))
            self.valorlitro = change

        def alterarcombustível():
            demanda = input("Escolha o combustível desejado: ")
            self.tipocombustível = demanda
        

