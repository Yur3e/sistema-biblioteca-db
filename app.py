from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
app.secret_key = "biblioteca123"  # usado para mensagens flash

# === Conexão com o MongoDB Atlas ===
client = MongoClient("mongodb+srv://Aprendendo_mongo:Aprendendo_mongo@aprendendomongo.yywviso.mongodb.net/?retryWrites=true&w=majority&appName=Aprendendomongo")
banco = client["biblioteca"]
usuarios = banco["usuarios"]
livros = banco["livros"]
autores = banco["autores"]

# ====================== ROTAS DE LOGIN ======================

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = usuarios.find_one({"email": email, "senha": senha})

        if usuario:
            flash(f"Bem-vindo(a), {usuario['nome']}!", "success")
            return redirect(url_for('painel'))
        else:
            flash("Email ou senha incorretos!", "error")

    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        # Verifica se o email já existe
        if usuarios.find_one({"email": email}):
            flash("Este e-mail já está cadastrado!", "error")
            return redirect(url_for('cadastro'))

        # Insere o novo usuário
        usuarios.insert_one({
            "nome": nome,
            "email": email,
            "senha": senha
        })

        flash("Cadastro realizado com sucesso! Faça login para continuar.", "success")
        return redirect(url_for('login'))

    return render_template('cadastro.html')

@app.route('/painel')
def painel():
    """Painel principal com os livros"""
    return render_template('index.html')

# ====================== ROTAS DE LIVROS ======================

@app.route('/api/livros', methods=['GET'])
def get_livros():
    """Retorna todos os livros com autor e imagem"""
    lista = []
    for livro in livros.find():
        autor = autores.find_one({"_id": livro["autor_id"]})
        lista.append({
            "id": str(livro["_id"]),
            "titulo": livro["titulo"],
            "ano_publicacao": livro["ano_publicacao"],
            "genero": livro["genero"],
            "autor": autor["nome"] if autor else "Desconhecido",
            "disponivel": livro["disponivel"],
            "imagem_url": livro.get("imagem_url", ""),
            "sinopse": livro.get("sinopse", "")
        })
    return jsonify(lista)

@app.route('/livro/<id>')
def detalhes_livro(id):
    """Renderiza a página de detalhes de um livro específico"""
    livro = livros.find_one({"_id": ObjectId(id)})
    if not livro:
        return "Livro não encontrado", 404

    autor = autores.find_one({"_id": livro["autor_id"]})
    return render_template('detalhes.html', livro=livro, autor=autor)

# ====================== EXECUÇÃO ======================

if __name__ == '__main__':
    app.run(debug=True)
