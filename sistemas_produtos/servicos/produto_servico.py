import sqlite3

class ProdutoServico:
    @staticmethod
    def conectar():
        # Conecta ao arquivo banco.db que aparece no seu projeto
        conn = sqlite3.connect('banco.db')
        conn.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome: produto['nome']
        return conn

    @classmethod
    def listar_produtos(cls):
        conn = cls.conectar()
        cursor = conn.cursor()
        # Executa o Processo mostrado no seu slide de "Listagem"
        cursor.execute("SELECT id, nome, descricao, preco FROM produtos")
        produtos = cursor.fetchall()
        conn.close()
        return produtos

    @classmethod
    def buscar_por_id(cls, id_produto):
        conn = cls.conectar()
        cursor = conn.cursor()
        # Executa o Processo mostrado no seu slide de "Busca por ID"
        cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
        produto = cursor.fetchone()
        conn.close()
        return produto

    @classmethod
    def criar(cls, nome, descricao, preco):
        conn = cls.conectar()
        cursor = conn.cursor()
        cursor.execute(
    "INSERT INTO produtos(nome, descricao, preco) VALUES (?, ?, ?)",
    (nome, descricao, preco)
)
        conn.commit()
        conn.close()

def inicializar_tabela():
    # Esta função cria a tabela caso o arquivo banco.db esteja vazio
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()