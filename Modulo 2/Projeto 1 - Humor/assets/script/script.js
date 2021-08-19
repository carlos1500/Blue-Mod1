const elementoIntro = document.querySelector('#texto')
const elementoImagem = document.querySelector('#arquivoImagem')
let elementoBotao = document.querySelector('#alterar')
let Lista = ['primeiro', 'segundo', 'terceiro','quarto', 'quinto', 'sexto']

elementoBotao.addEventListener('click', () => {
    if (elementoBotao.value == 'primeiro') {
        elementoImagem.src = './assets/img/gótica.jpg'
        elementoIntro.innerText = 'O seu humor é: Gretchen Gótica! \nVocê é intensa e profunda. Uma amiga leal, mas que  Poucas pessoas compreendem.\nTente evitar ficar mais desanimada do que já é. \nAproveite o clima para um boa taça de vinho.'
        elementoBotao.value = 'segundo'
    }

    else if (elementoBotao.value == 'segundo') {
        elementoImagem.src = './assets/img/dança.gif'  
        elementoIntro.innerText = 'O seu humor é: Gretchen Dançarina\nVocê é animada e divertida, a verdadeira alma da festa \n Continue sempre com seu CongaLaConga, mas cuidado para não abusar do álcool!'
        elementoBotao.value = 'terceiro' 
    }
    else if (elementoBotao.value == 'terceiro') {
        elementoImagem.src = './assets/img/indignada.png'
        elementoIntro.innerText = 'O seu humor é: Gretchen indignada!\n Você não aceita desaforo e está sempre pronta para defender o que acredita\n Está ouvindo esse som? É o tabu sendo quebrado!'
        elementoBotao.value = 'quarto'
    }
    else if (elementoBotao.value == 'quarto'){
        elementoImagem.src = './assets/img/grata.jpg'
        elementoIntro.innerText = 'O seu humor é: Gretchen Gratiluz!\nVocê é muito grata pela natureza, os animaizinho e as flores\n Cotinue com a essa vibe boa, mas atenção! Nem tudo quen é natural faz bem\nCuidado com as ervas, garota!'
        elementoBotao.value = 'quinto'
    }

    else if (elementoBotao.value == 'quinto'){
        elementoImagem.src = './assets/img/samba.gif'
        elementoIntro.innerText = 'O seu humor é: Gretchen Brasileira!\nVocê adora um samba, um futebol e uma caipirinha\nAproveite o Carnaval e beije muito!\nO ministério da saúde adverte: #UseCamisinha'
        elementoBotao.value = 'sexto'
    }
})