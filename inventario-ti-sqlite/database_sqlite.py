import sqlite3

def inicializar_banco():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ativos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            responsavel TEXT,
            setor TEXT,
            tipo TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vulnerabilidades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_ativo INTEGER,
            descricao TEXT,
            categoria TEXT,
            severidade TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def salvar_ativo(id, nome, responsavel, setor, tipo):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ativos VALUES (?, ?, ?, ?, ?)", (id, nome, responsavel, setor, tipo))
    conn.commit()
    conn.close()

def buscar_ativo(id):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ativos WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "nome": row[1], "responsavel": row[2], "setor": row[3], "tipo": row[4]}
    return None

def buscar_ativo_por_nome(nome):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ativos WHERE nome = ?", (nome,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "nome": row[1], "responsavel": row[2], "setor": row[3], "tipo": row[4]}
    return None

def atualizar_ativo(id, nome, responsavel, setor, tipo):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE ativos SET nome=?, responsavel=?, setor=?, tipo=? WHERE id=?
    """, (nome, responsavel, setor, tipo, id))
    conn.commit()
    conn.close()

def remover_ativo(id):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ativos WHERE id = ?", (id,))
    cursor.execute("DELETE FROM vulnerabilidades WHERE id_ativo = ?", (id,))
    conn.commit()
    conn.close()

def salvar_vulnerabilidade(id_ativo, descricao, categoria, severidade, status):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO vulnerabilidades (id_ativo, descricao, categoria, severidade, status)
        VALUES (?, ?, ?, ?, ?)
    """, (id_ativo, descricao, categoria, severidade, status))
    conn.commit()
    conn.close()

def carregar_vulnerabilidades(id_ativo):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vulnerabilidades WHERE id_ativo = ?", (id_ativo,))
    rows = cursor.fetchall()
    conn.close()
    vulnerabilidades = {}
    for row in rows:
        vulnerabilidades[row[0]] = {
            "id": row[0],
            "id_ativo": row[1],
            "descricao": row[2],
            "categoria": row[3],
            "severidade": row[4],
            "status": row[5]
        }
    return vulnerabilidades
def remover_vulnerabilidade(id_vuln):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM vulnerabilidades WHERE id = ?", (id_vuln,))
    conn.commit()
    conn.close()
