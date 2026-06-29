# Stock Control CLI

Um sistema de controle de estoque via terminal feito com Python e PostgreSQL. Dá pra cadastrar, visualizar, atualizar e deletar produtos direto pelo terminal.

## Tecnologias

- Python 3.12
- PostgreSQL
- psycopg2
- python-dotenv

## Como rodar

Clone o repositório e instale as dependências:

\```bash
git clone https://github.com/seu-usuario/stock-control-cli.git
cd stock-control-cli
pip install psycopg2-binary python-dotenv
\```

Crie um arquivo `.env` na raiz do projeto:

\```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=produtos
DB_USER=postgres
DB_PASS=suasenha
\```

Crie a tabela no seu banco PostgreSQL:

\```sql
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    preco NUMERIC(10, 2)
);
\```

Depois é só rodar:

\```bash
python main.py
\```

## Funcionalidades

- Cadastrar produto
- Ver um produto pelo ID
- Ver todos os produtos
- Atualizar um produto
- Deletar um produto
