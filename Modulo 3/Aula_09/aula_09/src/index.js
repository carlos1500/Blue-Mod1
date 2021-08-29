import React, { useState , useEffect} from 'react';
import ReactDOM from 'react-dom';
import './index.css';

export default function Home(){
  return <h1>Calculadora IMC</h1>
}

export function Peso(props){
var peso = <textarea placeholder="Digite o seu peso atual"> </textarea>
var altura = <textarea placeholder="Digite a sua altura"></textarea>
return peso / altura
}


ReactDOM.render(
  <React.StrictMode>
    <Home />
    <Peso />
  </React.StrictMode>,
  document.getElementById('root')
);
