#1) Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula anterior, crie um lançador de dados e moedas em que o usuário deve escolher o objeto a ser lançado. Não esqueça que os lançamentos são feitos de forma randômica.

import random

class Lançador():

    def __init__(self, escolha):
        self.escolha = escolha.upper()
        self.escolher()      

    def lançarDado (self):
        r = random.randint(1,6)
        print(f"O dado sorteou o numero {r}.")

    def lançarMoeda(self):
        r = random.randint(1,2)
        if r == 1:
            r = "Cara"
        else:
            r = "Coroa"        
        print(f"Moeada caiu {r}.")

    def escolher (self):
        if self.escolha == "DADO":
            self.lançarDado()
        else:
            self.lançarMoeda()    

l = input("Escolha oque vc deseja lançar. DADO ou MOEDA: ")
lançar = Lançador(l)



