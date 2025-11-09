from flask import Flask, render_template, request, redirect, url_for, flash, session
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
app.secret_key = "biblioteca123"  # usado para mensagens flash e sessão

# === Conexão com o MongoDB Atlas ===
client = MongoClient("mongodb+srv://Aprendendo_mongo:Aprendendo_mongo@aprendendomongo.yywviso.mongodb.net/?retryWrites=true&w=majority&appName=Aprendendomongo")
banco = client["biblioteca"]
usuarios = banco["usuarios"]
livros = banco["livros"]
autores = banco["autores"]

# ====================== ROTAS DE LOGIN / CADASTRO ======================

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Tela de login"""
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = usuarios.find_one({"email": email, "senha": senha})

        if usuario:
            session['usuario_id'] = str(usuario['_id'])
            session['usuario_nome'] = usuario['nome']
            flash(f"Bem-vindo(a), {usuario['nome']}!", "success")
            return redirect(url_for('home'))
        else:
            flash("Email ou senha incorretos!", "error")

    return render_template('login.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    """Tela de cadastro de novo usuário"""
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        # Verifica se o email já existe
        if usuarios.find_one({"email": email}):
            flash("Este e-mail já está cadastrado!", "error")
            return redirect(url_for('cadastro'))

        usuarios.insert_one({
            "nome": nome,
            "email": email,
            "senha": senha
        })

        flash("Cadastro realizado com sucesso! Faça login para continuar.", "success")
        return redirect(url_for('login'))

    return render_template('cadastro.html')


@app.route('/logout')
def logout():
    """Efetua logout e limpa sessão"""
    session.clear()
    flash("Você saiu da sua conta.", "success")
    return redirect(url_for('login'))

# ====================== ROTAS DE LIVROS ======================

@app.route('/')
def home():
    """Renderiza a página inicial com os livros"""
    if 'usuario_id' not in session:
        flash("Faça login para acessar a biblioteca.", "error")
        return redirect(url_for('login'))
    
    todos_livros = []
    for livro in livros.find():
        autor = autores.find_one({"_id": livro["autor_id"]})
        todos_livros.append({
            "_id": str(livro["_id"]),
            "titulo": livro["titulo"],
            "ano_publicacao": livro["ano_publicacao"],
            "genero": livro["genero"],
            "autor": autor["nome"] if autor else "Desconhecido",
            "disponivel": livro["disponivel"],
            "imagem_url": livro.get("imagem_url", ""),
            "sinopse": livro.get("sinopse", "")
        })

    return render_template('index.html', livros=todos_livros)


@app.route('/livro/<id>')
def detalhes_livro(id):
    """Renderiza a página de detalhes de um livro específico"""
    if 'usuario_id' not in session:
        flash("Faça login para ver os detalhes do livro.", "error")
        return redirect(url_for('login'))

    livro = livros.find_one({"_id": ObjectId(id)})
    if not livro:
        return "Livro não encontrado", 404

    autor = autores.find_one({"_id": livro["autor_id"]})
    return render_template('detalhes.html', livro=livro, autor=autor)

# ====================== EXECUÇÃO ======================

if __name__ == '__main__':
    app.run(debug=True)
