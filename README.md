# 📚 Sistema de Biblioteca Online

Este projeto é um *Sistema de Biblioteca Online* desenvolvido com *Python* e MongoDB Atlas, que permite o gerenciamento de livros, autores e empréstimos.  
O sistema foi criado como parte do projeto da disciplina *Banco de Dados NoSQL*.

---

## 🚀 Tecnologias Utilizadas

- *Python 3*
- *MongoDB Atlas* (Banco de Dados na Nuvem)
- *Flask* (para a interface web)
- *pymongo* (conexão com o MongoDB)
- *HTML / CSS* (para o front-end das páginas)

---

## 🎯 Funcionalidades

- Registro de *empréstimos* e *devoluções*
- Login de usuários (interface funcional)
- Cadastro de usuários (interface funcional)
- Apenas registro de empréstimo sem devolução com função visual
- Visualização do acervo disponível

---

## 🗂 Estrutura do Banco de Dados (MongoDB)

O banco de dados foi criado no *MongoDB Atlas*, com o nome biblioteca, contendo as coleções:

- autores → guarda informações dos autores
- livros → guarda informações sobre cada livro
- emprestimos → registra os empréstimos realizados

Exemplo de criação no Python:

```python
from pymongo import MongoClient

client = MongoClient("sua_string_de_conexao_mongodb")
db = client["biblioteca"]

autores = db["autores"]
livros = db["livros"]
emprestimos = db["emprestimos"]