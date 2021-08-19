const express = require("express");
const app = express();

const port = 4100;

app.use(express.json());

const filmes = [
  "Donnie Darko",
  "Bonequinha de Luxo",
  "Dançando no Escuro",
  "Bruna Surfistinha",
];

app.get("/", (req, res) => {
  res.send("Bonjour");
});

app.get("/filmes", (req, res) => {
  res.send(filmes);
});

app.get("/filmes/:id", (req, res) => {
  const id = req.params.id - 1;
  const filme = filmes[id];

  if (!filme) {
    res.send("Filme não encontrado");
  }
});

app.post("/filmes", (req, res) => {
  const filme = req.body.filme;
  const id = filmes.length;
  filmes.push(filme);

  res.send(`filme adicionado com sucesso: ${filme}. O Id do filme é ${id}`);
});

app.put("/filmes/:id", (req, res) => {
  const id = req.params.id - 1;
  const filme = req.body.filme;
  filmes[id] = filme;
  res.send(`filme atualizado com sucesoo: ${filme}.`);
});

app.delete("/filmes/:id", (req, res) => {
  const id = req.params.id - 1;
  const filme = filmes[id]; 
  if (filme) {
    delete filmes[id];
    res.send(`filme excluído com sucesso`);
  } else res.send("Filme não localizado");
});

app.listen(port, function () {
  console.info(`app rodando na porta: http://localhost:${port}/`);
});
