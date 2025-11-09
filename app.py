from flask import Flask, jsonify, render_template
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# Conexão com o MongoDB Atlas
client = MongoClient("mongodb+srv://Aprendendo_mongo:Aprendendo_mongo@aprendendomongo.yywviso.mongodb.net/?retryWrites=true&w=majority&appName=Aprendendomongo")
banco = client['biblioteca']
livros = banco['livros']
autores = banco['autores']

@app.route('/api/livros', methods=['GET'])
def get_livros():
    """Retorna todos os livros"""
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
            "imagem_url": livro.get("imagem_url", ""),  # nova chave
            "sinopse": livro.get("sinopse", "")
        })
    return jsonify(lista)

@app.route('/')
def home():
    """Renderiza a página inicial"""
    return render_template('index.html')

@app.route('/livro/<id>')
def detalhes_livro(id):
    """Renderiza a página de detalhes de um livro específico"""
    livro = livros.find_one({"_id": ObjectId(id)})
    if not livro:
        return "Livro não encontrado", 404
    
    autor = autores.find_one({"_id": livro["autor_id"]})
    return render_template('detalhes.html', livro=livro, autor=autor)

if __name__ == '__main__':
    app.run(debug=True)
