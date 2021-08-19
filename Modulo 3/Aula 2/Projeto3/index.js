const express = require('express');
const app = express();

const port = 4890;

const jogos = [
    "The Sims",
    "Super Mário",
    "GTA - San Andreas",
    "GTA -V",
    "Cobrinha",
    "Guitar Hero",
    
    
    
];

app.get('/', (req, res) => {
    res.send('Games Monster')
});

app.get('/jogos', (req, res) => {
    res.send(jogos);
});

app.get('/jogos/:id', (req, res) => {
    const id = req.params.id -1;
    const jogo = jogos[id];
    res.send(jogo)
});


function randomMinMax(min, max) {
    return Math.floor(Math.random() * (max -min)) + min;
};


app.get('/jogododia', (req, res) =>{
    res.send(`${jogos[randomMinMax(0, jogos.length)]}`); 
});


app.listen(port, () => {
    console.info(`App está rodando em: http://localhost:${port}/`);
});