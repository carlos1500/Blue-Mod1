const express = require('express');
const app = express();

const port = 3390;

app.use(express.json());


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

app.post('/jogos', (req, res) => {
    const jogo = req.body.jogo;
    const id = jogos.length;
    jogos.push(jogo);

    res.send(`jogo: ${jogo} adicionado com sucesso!`)
});

app.put('/jogos/:id', (req,res) => {
    const id = req.params.id -1;
    const jogo = req.body.jogo;
    jogos[id] = jogo;
    res.send(`O jogo: ${jogo}, foi atualizado com sucesso`);
});

app.delete('/jogos/:id', (req,res)=>{
    const id = req.params.id -1;
    const jogo = jogos[id];
    if (!jogo) {
        res.send('jogo não localizado')
    }
    jogos.splice(jogo, 1)
    res.send(`Jogo deletado com sucesso`)

})

app.listen(port, () => {
    console.info(`App está rodando em: http://localhost:${port}/`)
});