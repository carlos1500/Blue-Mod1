def autoriza_voto(nasc):
    idade = 2021 - nasc
    if idade > 15 and idade <18:
        return "opcional"
    elif idade > 17 and idade < 70:
        return "obrigatório"
    elif idade > 70:
        return "opcional"
    else:
        return "negado"

def votacao(autoriza, voto):
    if autoriza == "negado":
        print(f"Desculpe, usuário não autorizado a votar. O usuário inserido tem menos de 16 anos de idade, e o voto é permitido em modalidade opcional a partir dos 16 anos. Mas não desanime, a democracia precisa do seu entuasiamo, retorne quando tiver pelo menos 16 anos.\n")
    else:
        return voto   
 

total_votos = []

while True:
        r = input(f"Bem vindo ao Sistema de Votações da Fenda do Biquíni. Deseja cadastrar mais um cidadão para votar? S/N:\n ").upper()
        if r == "N":
            break
        else:
            Entrada = autoriza_voto(int(input(f"Por favor. Digite o ano de seu nascimento: \n")))
            voto = int(input(f"Os candadatos à eleição são:\n1 - Lula Molusco \U0001F419\n2 - Bob Esponja \U0001F9FD\n3 - Sirigueijo \U0001F980\n4 - Voto Branco \U0001F3F3\n5 - Voto Nulo. \U0001F6AB\nPor favor. Digite o número referente ao seu candidato: "))

            eleição = votacao(Entrada, voto)
            votos = total_votos.append(eleição)

candidatos = {"lula molusco \U0001F419": 0, "bob esponja \U0001F9FD": 0, "sirigueijo \U0001F980": 0, "voto branco \U0001F3F3": 0, "voto nulo \U0001F6AB": 0}

for i in total_votos:    
    if i == 1:
        candidatos ["lula molusco"] += 1
    elif i  == 2:
        candidatos ["bob esponja"] += 1
    elif i == 3:
        candidatos ["sirigueijo"] += 1
    elif i == 4:
        candidatos ["voto branco"] += 1
    elif i == 5:
        candidatos ["voto nulo"] += 1

print(candidatos)

candidatos = {value:key for key, value in candidatos.items()}
vencedor = (max(candidatos.keys()))

print()
print("O vencedor da eleição de Imperador Supremo da Vila Fenda do Biquini é: ")
print(candidatos[vencedor])

print("Parabéns! A festa de coroação ocorrerá no Siricascudo")


    
    

