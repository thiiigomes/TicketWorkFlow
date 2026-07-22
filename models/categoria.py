from database.connection import get_connection


def listar_categorias():

    conexao = get_connection()

    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id,
            nome
        FROM categoria
        ORDER BY nome
    """)

    categorias = cursor.fetchall()

    cursor.close()
    conexao.close()

    return categorias