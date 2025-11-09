document.addEventListener("DOMContentLoaded", async () => {
    const container = document.getElementById("livros-container");
    container.innerHTML = "<p>Carregando livros...</p>";

    try {
        const response = await fetch("/api/livros");
        const livros = await response.json();

        if (livros.length === 0) {
            container.innerHTML = "<p>Nenhum livro encontrado.</p>";
            return;
        }

        container.innerHTML = "";
        livros.forEach(livro => {
            const card = document.createElement("div");
            card.className = "livro";

            card.innerHTML = `
                <img src="${livro.imagem_url}" alt="${livro.titulo}" class="livro-img">
                <h3>${livro.titulo}</h3>
                <p><strong>Autor:</strong> ${livro.autor}</p>
                <p><strong>Gênero:</strong> ${livro.genero}</p>
                <a href="/livro/${livro.id}" class="btn-detalhes">Ver detalhes</a>
            `;

            container.appendChild(card);
        });
    } catch (error) {
        container.innerHTML = "<p>Erro ao carregar os livros.</p>";
        console.error(error);
    }
});
