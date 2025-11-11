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

- Registro de *empréstimos* sem devolução com função visual
- Login de usuários (interface funcional)
- Cadastro de usuários (interface funcional)
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
```

---

## 🔗 Modelo de Dados: Referencing (Referência)

O modelo adotado neste projeto é o *Referencing, ou seja, os relacionamentos entre coleções são representados por **referências (IDs)*, e não pelo armazenamento de dados dentro de outros documentos.

### 🧠 O que é o modelo Referencing?

O *Referencing* é utilizado quando existe uma *relação 1:N* (um autor pode ter vários livros).  
Nesse modelo, o documento “filho” (livro) guarda apenas o *ID do documento pai* (autor), em vez de duplicar todos os dados do autor.

---

## 💻 Como Executar o Projeto

Siga os passos abaixo para executar o sistema localmente:

### 📍 Clone o repositório
bash
git clone https://github.com/seuusuario/sistema-biblioteca.git


### 📍 Instale as dependências
bash
pip install flask pymongo


### 📍 Configure o MongoDB Atlas
Edite o arquivo app.py e substitua a string de conexão:
python
client = MongoClient("sua_string_de_conexao_mongodb")


### 📍 Execute o servidor Flask
bash
python app.py


### 📍 Acesse no navegador

http://localhost:5000


Você será redirecionado para a *página de login*, e poderá navegar entre o painel e as rotas do sistema.

---

## 🧰 Estrutura do Projeto


📁 sistema-biblioteca
├── app.py

├── templates/

│   ├── login.html

│   ├── cadastro.html

│   ├── emprestimo.html

│   └── index.html

├── static/

│   ├── css/

│   └── img/

└── README.md


---

## 👩‍🏫 Projeto Acadêmico

📘 *Trabalho da disciplina:* Banco de Dados NoSQL  
👩‍🏫 *Professora:* Jessily Medeiros Quaresma 
🎓 *Curso:* Ciência de Dados  
👩‍💻 *Desenvolvido por:* Ayryslaine Kelle, Brenno Vale, Caio Henrique, José Yure e Jeová Anderson

📅 *Ano:* 2025  
🏫 *Instituição:* Universidade Estadual da Paraíba

---

> 💬 Este projeto foi desenvolvido com fins educacionais para demonstrar o uso do modelo de dados Referencing no MongoDB em um sistema web completo de gerenciamento de biblioteca.
