const express = require('express');
const app = express();

const port = 3890;

const jogos = [
    "The Sims",
    "Super Mário",
    "GTA - San Andreas",
    
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
})

app.listen(port, () => {
    console.info(`App está rodando em: http://localhost:${port}/`)
});