#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário incluindo o total de gols feitos durante o campeonato.

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

    def somaGols(self):
        self.gols['totalGols'] = sum(self.gols['golsPartida'])

    def mostraDic(self):
        return self.gols

nome = input('Nome do jogador: ')
partidas = int(input('Quantas partidas: '))

j1 = Jogador(nome, partidas)
j1.contagemGols()
print(j1.mostraDic())
