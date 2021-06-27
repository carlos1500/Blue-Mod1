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
        print(f"Desculpe, usuário não autorizado a votar. O usuário inserido tem menos de 16 anos de idade, e o voto é permitido em modalidade opcional a partir dos 16 anos. Mas não desanime, a democracia precisa do seu entuasiamo, retorne quando tiver pelo menos 16 anos.")
    else:
        return voto   
 

total_votos = []

while True:
        r = input(f"Bem vindo ao Sistema de Votações da Fenda do Biquíni. Deseja cadastrar mais um cidadão para votar? S/N:\n ").upper()
        if r == "N":
            break
        else:
            Entrada = autoriza_voto(int(input(f"Por favor. Digite o ano de seu nascimento: \n")))
            voto = int(input(f"Os candadatos à eleição são:\n1 - Lula Molusco\n2 - Bob Esponja\n3 - Sirigueijo\n4 - Voto Branco\n5 - Voto Nulo. \nPor favor. Digite o número referente ao seu candidato: "))

            eleição = votacao(Entrada, voto)
            votos = total_votos.append(eleição)

print(total_votos)

candidatos = [{"lula molusco": 0}, {"bob esponja": 0}, {"sirigueijo": 0}, {"voto nulo": 0}, {"voto branco": 0}]

for i in total_votos:    
    if i == 1:
        candidatos[0] ["lula molusco"] += 1
    elif i  == 2:
        candidatos[1] ["bob esponja"] += 1
    elif i == 3:
        candidatos[2] ["sirigueijo"] += 1
    elif i == 4:
        candidatos[3] ["voto nulo"] += 1
    elif i == 5:
        candidatos[4] ["voto branco"] += 1

print(f"O total de votos foi: \n{candidatos[0]}\n{candidatos[1]}\n{candidatos[2]}\n{candidatos[3]}\n{candidatos[4]}")
    
    

