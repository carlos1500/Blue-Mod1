#Classe dos personagens não jogáveis (non-player character)
from personagem import Personagem
import random
import os

class Npc(Personagem):

    def __init__(self, nome, sexo):
        super().__init__(nome, sexo)
        self.alimento = 50
        self.cofre = 50
        

    def abrirEstoque(self):
        
        sorteio = random.randint(0, 50)

        if sorteio < 100:

            print ("\nParece que Hebe tem um estoque de comida guardado! Quando você clica na fechadura eletrônica a seguinte mensagem aparece:\n\n'Olá gracinha! para abrir o estoque responda a charada: Meu avô tem 5 filhos, cada filho tem 3 filhos. Quantos primos eu tenho?'\nQue velha doida, né?\n")
            
            while True:
                try:
                    print("De qualquer forma digite a resposta para abrir o estoque: \n")
                    resp = int(input())
                    break
                except:
                    print("\nOpção invalida. Digite apenas numeros: \n")

            if resp == (12):
                print("\nDeu certo! \n")
                return self.alimento
            else:
                print("\nA senha está errada e o alarme disparou! \n")
               
       

    def abrirCofre(self):

        lista = list(range(50))
        sorteio = random.randint(0, 99)

        if sorteio in lista:

            print ("\nQue sorte! No meio das pilhas de ferramentas você encontrou um cofre! Provavelmente é do dono Xaropinho\nEmbaixo do cofre está um papel escrito:\n\n'rapaiz... senha: 2683'\n\n(Claramente, ele não entende muito de segurança, não é mesmo?) Mas parece que os ratos roeram o quinto número do papel. \nVale a pena chutar alguns números para abrir o cofre!\n")

            for i in range(5):
                tentativas = 4 - i
                senha = 1
                while True:
                    try:
                        print("Digite o ultimo digito dessa senha: ")
                        chute = int(input())
                        break
                    except:
                        print("\nOpção invalida. Digite apenas numeros: \n")

                if senha == chute:
                    print("\nParabens!!! Você acertou a senha!!! \n") 
                    return self.cofre
                else:
                    if tentativas > 0:
                        print(f"\nSenha incorreta. Você tem mais {tentativas} tentativas: \n")
                    else:
                        print()
                    
        print("\nVc não conseguiu abrir o cofre! \n")
        

    


    
                

