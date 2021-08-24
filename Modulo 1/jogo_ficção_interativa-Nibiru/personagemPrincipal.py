from personagem import Personagem
from personagemnpc import Npc
from tempo import Tempo
import random
import os

class PersonagemPrincipal(Personagem):

    npc1 = Npc("Hebe", "F")
    npc2= Npc("Xaropinho", "F")
    tempo = Tempo()
    cont1 = 0
    cont2 = 0
    

    def __init__(self, nome, sexo):
        super().__init__(nome, sexo)
        self.stamina = 10
        self.inventario = {"Alimento":0, "Equipamento":0}    


    def getAlimento(self):
        return self.inventario  ["Alimento"]  

    def getEquipamento(self):
        return self.inventario ["Equipamento"]    
    

    #Função de buscar alimentos para adicionar ao estoque do inventário
    def buscarAlimento(self):
        
        self.cond = False

        resposta = self.menuAlimentos()

        # gasto de stamina varia de acordo com a escolha da ação, ações mais garantidas gastam mais stamina.
        if resposta == 1 and self.stamina >= 3:
            self.stamina -= 3
            self.tempo.passarHora(4)
            if self.tempo.getDia() >= 3:
                return 
        elif resposta == 2 and self.stamina >= 1:
            self.stamina -= 1
            self.tempo.passarHora(1)
            if self.tempo.getDia() >= 3:
                return 
        elif resposta == 3 and self.stamina >= 3:
            self.stamina -= 2     
            self.tempo.passarHora(2)
            self.estoqueNPC()
            if self.tempo.getDia() >= 3:
                return 
        else:
            resposta = 0
            self.cond = self.fimStamina()
            
        # quantidade de alimento conseguida na ação, varia de acordo com o resultado do sorteio:

        sorteio = random.randint(1,3)

        if sorteio == 1:
            a = 8
        elif sorteio == 2:
            a = 2
        elif sorteio == 3:
            a = 4              
        if self.cond == False:
            if resposta == sorteio:
                self.inventario ["Alimento"] += a
                print(f"\nParabens, você conseguiu {a} alimentos")
            else:
                print("\nPoxa, que falta de sorte, não foi dessa vez!")    

        print("\nEnter para continuar")
        input()
        os.system('cls')   



    #Função para buscar equipamentos 
    def buscarEquipamentos(self):

        self.cond = False

        resposta = self.menuEquipamentos()
        
        # Gasto de stamina de acordo com a escolha da ação
        if resposta == 1 and self.stamina >= 2:
            self.stamina -= 2
            self.tempo.passarHora(1)
            self.cofreNPC()
            if self.tempo.getDia() >= 3:
                return 
        elif resposta == 2 and self.stamina >= 5:
            self.stamina -= 5
            self.tempo.passarHora(4)
            if self.tempo.getDia() >= 3:
                return 
        elif resposta == 3 and self.stamina >= 3:
            self.stamina -= 3  
            self.tempo.passarHora(2)
            if self.tempo.getDia() >= 3:
                return 
        else:
            resposta = 0
            self.cond = self.fimStamina()
            
    # quantidade de equipamento varia de acordo com o sorteio.

        sorteio = random.randint(1,3)

        if sorteio == 1:
            e = 2
        elif sorteio == 2:
            e = 8
        elif sorteio == 3:
            e = 4 

        if self.cond == False:
            if resposta == sorteio:
                self.inventario ["Equipamento"] += e 
                print(f"\nParabens, você conseguiu {e} equipamentos")
            else:
                print("\nPoxa, que falta de sorte, não foi dessa vez!")  

        print("\nEnter para continuar")
        input()
        os.system('cls')     
            

    def menuAlimentos(self):
        while True:
            print()
            print("Digite 1 para ir caçar")
            print("Digite 2 para pedir comida da rua")
            print("Digite 3 para roubar do vizinho")
            print()
            try:
                resposta = int(input())
                if 0 < resposta < 4:
                    return resposta
                else:
                    print('\nOpção inválida! \n')
            except:
                print("\nOpção invalida. Digite apenas numeros: \n")


    def menuEquipamentos(self):
        while True:
            print()
            print("Digite 1 para buscar no ferro velho")
            print("Digite 2 para fabricar peças")
            print("Digite 3 para roubar peças")
            print()
            try:
                resposta = int(input())
                if 0 < resposta < 4:
                    return resposta
                else:
                    print('\nOpção inválida!\n')
            except:
                print("\nDigite apenas números!\n")


    def fimStamina(self):
        print("\nOpa! Parece que você não tem stamina para concluir essa tarefa\n")
        if self.inventario ["Alimento"] > 0:             
            while True:
                print("\nDeseja comer para recuperar stamina? [S/N] \n")
                resp = input()[0].lower().strip()
                if resp in ['s', 'n']:
                    break
                else:
                    print('\nOpção Inválida!\n')
            if resp == 's': 
                while True:
                    print("\nQual a quantidade de alimentos para comer? \n")
                    try:
                        c = int(input())
                        if c < 1 or c > self.inventario['Alimento']:
                            print('\nDigite uma quantidade válida!\n')
                        else:
                            self.comer(c)
                            break
                    except:
                        print('\nDigite apenas números!\n')      
            
            elif resp == 'n':
                while True:
                    print("\nDeseja dormir para recuperar stamina? [S/N] \n")
                    resp = input()[0].lower().strip()
                    if resp in ['s', 'n']:
                        break
                    else:
                        print('\nOpção Inválida!\n')
                if resp == 's':
                    while True:
                        print("\nQuantas horas deseja dormir? \n")
                        try:
                            d = int(input())
                            break
                        except:
                            print('\nDigite apenas números!\n')
                    self.dormir(d)
                    
                elif resp == 'n':
                    print("\nVocê desmaiou pois estava sem energia!")
                    print("Amanhã você vai acordar com a stamina completa\n") 
                    self.desmaiar()
                                    
        else:      
            while True:
                print("\nDeseja dormir para recuperar energia? [S/N] \n")
                resp = input()[0].lower().strip()
                if resp in ['s', 'n']:
                    break
                else:
                    print('\nOpção Inválida!\n')
            if resp == 's':
                while True:
                    print("\nQuantas horas deseja dormir? \n")
                    try:
                        d = int(input())
                        break
                    except:
                        print('\nDigite apenas números!\n')
                self.dormir(d)
            elif resp == 'n':
                print("\nVocê desmaiou pois estava sem energia!")
                print("Amanhã você vai levantar com a stamina completa\n") 
                self.desmaiar()

        return True       



    def relogio (self):     #Função de controle da passagem do tempo.
        return self.tempo.getDia()


    def comer (self, comida): #função de busca de alimento para o inventário. 
        self.inventario ["Alimento"] -= comida       
        self.stamina += comida

        
    def dormir(self, horasDormidas): #Função usada para recuperar a stamina. 
        self.tempo.passarHora(horasDormidas)
        self.stamina += horasDormidas
        if self.stamina >= 10:
            self.stamina = 10
    

    def desmaiar(self): #Função chamada quando o usuário fica compeltamente sem energia e não dorme.
        self.stamina = 8
        self.tempo.passarHora(8)


    #Funções de inventário dos npc's.
    def estoqueNPC(self):
        if self.cont1 == 0:
            v = self.npc1.abrirEstoque()
            if v != None:
                self.inventario ["Alimento"] += v
                self.cont1 +=1


    def cofreNPC(self):
        if self.cont2 == 0:
            v = self.npc2.abrirCofre()
            if v != None:
                self.inventario ["Equipamento"] += v
                self.cont2 +=1        
      


    #Função de retorno do inventário. 
    def info(self):

        print("Aqui estão as suas informações essenciais, elas permitem que você planeje suas tarefas, fique atento a elas!")
        print()
        print(f"A quantidade de itens no seu inventário é: {self.inventario}. \n\nVocê precisa de no mínimo 20 itens de Alimento e 20 itens de Equipamentos para efetuar sua viagem com sucesso.")
        tempoRestante = 3 - self.tempo.getDia()
        print(f"Hoje é dia: {self.tempo.getDia()}, você tem apenas mais {tempoRestante} para finalizar suas tarefas!")
        print()
<<<<<<< HEAD
        print(f"Agora são: {self.tempo.getHora()} horas. \U0001F570")
        print(f"Sua stamina é: {self.stamina} \U0001F525")
=======
        print(f"Agora são: {self.tempo.getHora()} horas.")
        print(f"Sua stamina é: {self.stamina}")
>>>>>>> e74aab5680631fa8ebde125220070942fe1b9395
        print()