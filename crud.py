from database import get_connection

def create_product(nome, preco):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO produtos (nome, preco) VALUES (%s, %s) RETURNING id', (nome, preco))
        row = cur.fetchone()
        conn.commit()
        print(f'Produto Cadastrado {row}')
    except Exception as e:
        conn.rollback()
        print(f'Erro {e}')
    finally:
        cur.close()
        conn.close()

def read_product(id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM produtos WHERE id = %s', (id,))
        row = cur.fetchone()
        print(f'Produto Encontrado {row}')
    except Exception:
        conn.rollback()
        print('Produto não encontrado')
    finally:
        cur.close()
        conn.close()

def read_all_products():
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM produtos')
        rows = cur.fetchall()
        print(f'Produtos Encontrados {rows}')
    except Exception:
        conn.rollback()
        print('Nenhum Produto Encontrado')
    finally:
        cur.close()
        conn.close()

def update(id, nome, preco):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('UPDATE produtos SET nome = %s, preco = %s WHERE id = %s', (nome, preco, id))
        conn.commit()
        print(f'Update feito')
    except Exception:
        conn.rollback()
        print('Não foi possível realizar o update')
    finally:
        cur.close()
        conn.close()

def delete(id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('DELETE FROM produtos WHERE id = %s', (id,))
        conn.commit()
        print(f'Produto {id} deletado')
    except Exception:
        conn.rollback()
        print('Produto não encontrado')
    finally:
        cur.close()
        conn.close()