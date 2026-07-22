from database.connection import get_connection


def listar_prioridades():

    conexao = get_connection()

    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id,
            nome
        FROM prioridade
        ORDER BY id
    """)

    prioridades = cursor.fetchall()

    cursor.close()
    conexao.close()

    return prioridades