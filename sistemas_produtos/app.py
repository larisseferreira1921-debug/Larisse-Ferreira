from flask import Flask, render_template, request, redirect, url_for
from servicos.produto_servico import ProdutoServico, inicializar_tabela

app = Flask(__name__)

# Cria a tabela e o banco.db automaticamente ao iniciar
inicializar_tabela()

@app.route('/')
def index():
    # ETAPA 5: Usando a função de listagem do slide
    lista = ProdutoServico.listar_produtos()
    return render_template('index.html', produtos=lista)

# Rota para EXIBIR o formulário (Igual ao  slide)
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# Rota para SALVAR os dados no banco (O que faz o sistema funcionar)
@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = float(request.form['preco'])
    ProdutoServico.criar(nome, descricao, preco)
    return redirect(url_for('index'))

@app.route('/produto/<int:id_produto>')
def detalhes(id_produto):
    # ETAPA 5: Função de Busca por ID com tratamento de erro
    prod = ProdutoServico.buscar_por_id(id_produto)
    if prod is None:
        return "<h1>Erro: Produto não encontrado!</h1>", 404
    return render_template('detalhes.html', produto=prod)

if __name__ == '__main__':
    app.run(debug=True)