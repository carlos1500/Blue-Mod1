from personagemPrincipal import PersonagemPrincipal
from interface import Interface
import os


#Classe de execução do jogo. 
class Jogo:

    personagem = PersonagemPrincipal("L.U.C.A", "M")
    interface = Interface()
     

    def jogar(self): #função das tarefas que o usuário deve realizar no decorrer do jogo
        
        os.system('cls') 
        print()
        self.interface.introducao()
        input()
        os.system('cls') 
        self.interface.instrucoes()
        input()
        os.system('cls') 
        
        while self.personagem.relogio() < 3: #passagem do tempo do jogo

            resposta = self.menuTarefas()

            if resposta == 1:
                os.system('cls')
                self.personagem.info()
                self.personagem.buscarAlimento()   
            elif resposta == 2:
                os.system('cls')
                self.personagem.info()
                self.personagem.buscarEquipamentos()

        os.system('cls')   
        self.fimDoJogo()    
                

    def menuTarefas(self):
        self.personagem.info()
       
        while True:
            print()
            print(f"{'LISTA DE TAREFAS':^23}")    
            print()
            print("1 - Buscar alimentos")
            print("2 - Buscar equipamentos")
            print()
            try:
                resposta = int(input())
                if resposta == 1 or resposta == 2:
                    return resposta
                else:
                    print('\nOpção invalida. Tente novamente: \n')
            except:
                print('\nOpção invalida. Tente novamente: \n')


    #Função de monitoramento dos parametros de finalização do jogo. Alimento + Ferramentas + tempo
    def fimDoJogo(self):

        if self.personagem.getAlimento() >= 20 and self.personagem.getEquipamento() >= 20:
            return self.interface.venceu()
        elif self.personagem.getAlimento() >= 20 and self.personagem.getEquipamento() < 20:
            return self.interface.perder1()
        elif self.personagem.getAlimento() < 20 and self.personagem.getEquipamento() >= 20:
            return self.interface.perder2()
        else:
            return self.interface.perder3()


    

        
        






    
