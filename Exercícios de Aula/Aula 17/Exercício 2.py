#2) Vamos aprimorar o código:  cadastro de jogador de futebol.py que foi desenvolvido no Code Lab da aula 14. Faça com que o seu código funcione para vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.

class Jogador():
    def __init__(self, nome, partidas):
        self.nome = nome.capitalize()
        self.partidas = partidas
        self.gols = {'nome': nome, 'partidas': partidas}

    def contagemGols(self):
        lista = []
        for p in range(self.partidas):
            golsPartida = int(input(f'Quantos gols na {p+1}ª partida: '))
            lista.append(golsPartida)
        self.gols['golsPartida'] = lista
        self.somaGols()
        self.media()

    def somaGols(self):
        self.gols['totalGols'] = sum(self.gols['golsPartida'])

    def mostraDic(self):
        return self.gols

    def media(self):
        media = self.gols["totalGols"] / self.partidas
        self.gols ["aproveitamento"] = media 
        
jogadores = []

while True:
    nome = input('Nome do jogador: ')
    partidas = int(input('Quantas partidas: '))
    j1 = Jogador(nome, partidas)
    j1.contagemGols()
    jogadores.append(j1.mostraDic()) 
    continuar = input("Cadastrar mais um: ").lower()
    if continuar == "s":
        pass
    else:
        break

print (jogadores)
