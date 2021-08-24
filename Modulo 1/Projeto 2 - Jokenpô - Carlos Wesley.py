# Utilizando os conceitos aprendidos até estruturas de repetição, crie um
# programa que jogue pedra, papel e tesoura (Jokenpô) com você.
# O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de
# vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha
# de quantidade de rodadas, se não finalize o programa.

import random
from typing import overload
cartas = ["pedra", "papel", "tesoura"]
from time import sleep
pontos_jogador = 0
pontos_pc = 0

while True:
        abertura = int(input("Olá, vamos jogar Jokenpô! Quantas rodadas você deseja jogar? "))
        for i in range(abertura):
                jogada_pessoa = input(f"Qual a sua escolha? Pedra, Papel ou Tesoura? \n").lower()
                sleep(0.5)
                jogada_pc = random.choice(cartas)
                print(f"a minha escolha é {jogada_pc}\n")
        
                if jogada_pessoa == "papel":
                        if jogada_pc == "papel":
                                print(f"empate!\n")
                        if jogada_pc == "tesoura":
                                print(f"Oba!Eu ganhei!\n")
                                pontos_pc += 1
                        if jogada_pc == "pedra":
                                print(f"poxa! você ganhou.\n")
                                pontos_jogador += 1
                
                if jogada_pessoa == "tesoura":
                        if jogada_pc == "papel":
                                print (f"poxa! Você ganhou!\n")
                                pontos_jogador +=1
                        if jogada_pc == "tesoura":
                                print(f"Empate!\n")
                        if jogada_pc == "pedra":
                                print (f"Oba! Eu ganhei.\n")
                                pontos_pc += 1

                if jogada_pessoa == "pedra":
                        if jogada_pc == "papel":
                                print(f"Oba! Eu ganhei.\n")
                                pontos_pc += 1
                        if jogada_pc == "tesoura":
                                print(f"Poxa... Você ganhou!\n")
                                pontos_jogador += 1
                        if jogada_pc == "pedra":
                                print(f"Empate!\n")

                sleep (1)

        print (f"Você fez {pontos_jogador} pontos e eu fiz {pontos_pc}")
        if pontos_jogador > pontos_pc:
                print("Você é o grande vencedor! Parabéns!")
        elif pontos_jogador < pontos_pc:
                print("Oba! Eu sou grande vencedor. Boa sorte na próxima vez!")
        else:
                print("Empatamos!")

        repetir = input("Deseja Jogar novamente? ").lower()
        if repetir == "não":
                print("Tudo bem!")
                break 


     


  


        
    

        
    
    
    
