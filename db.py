import sqlite3

def create_connection():
    conn = sqlite3.connect("dados.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            preco TEXT,
            link TEXT
        );
    """)
    conn.commit()
    conn.close()

def inserir_produto(titulo, preco, link):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO produtos (titulo, preco, link)
        VALUES (?, ?, ?)
    """, (titulo, preco, link))
    conn.commit()
    conn.close()