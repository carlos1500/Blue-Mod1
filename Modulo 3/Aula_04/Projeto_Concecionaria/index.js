const express = require('express');
const app = express();

const port = 3001;

app.use(express.json());


const modelo = [
    'Nova Toyota Hilux',
    'Volkswagen Nivus',
    'Ford Territory',
    'Honda Civic',
    'BMW Série 2 Gran Coupé',
    'Nissan Versa',
]

const marca = [
    'Toyota',
    'Volkswagen',
    'Ford',
    'Honda',
    'BMW',
    'Nissan'
 ]

const cor = [
    'vermelho',
    'verde',
    'preto',
    'prata',
    'azul',
    'branco',
]

 const combustivel = [
    'gasolina',
    'álcool',
    'híbrido',
    'híbrido',
    'álcool',
    'gasolina'
 ]

app.get("/", (req, res)=>{
    res.send('Dinossauros');
});

app.get("/carros", (req,res) =>{
    res.send(`${modelo}, ${marca}, ${cor}, ${combustivel}`);
});

app.get("/carros/:id", (req,res) =>{
    const id = req.params.id -1;
    res.send(`${modelo[id]}, ${marca[id]}, ${cor[id]}, ${combustivel[id]}`);
});

app.post("/carros", (req,res) =>{
    const modelonovo = req.body.modelonovo;
    const marcanova = req.body.marcanova;
    const cornova = req.body.cornova;
    const combustivelnovo = req.body.combustivelnovo;

    const id = modelo.lenght;

    modelo.push(modelonovo)
    marca.push(marcanova)
    cor.push(cornova)
    combustivel.push(combustivelnovo)

    res.send(`O Carro: ${modelonovo}, da marca: ${marcanova}, da cor ${cornova} foi adicionado com sucesso!`)
})

app.put("/carros/:id", (req,res)=>{
    const id = req.params.id;
    
})


 app.listen(port, function () {
    console.info(`app rodando na porta: http://localhost:${port}/`);
  });