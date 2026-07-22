from database.connection import get_connection


def listar_equipamentos():

    conexao = get_connection()

    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id,
            CONCAT(fabricante, ' ', modelo) AS nome
        FROM equipamento
        ORDER BY fabricante, modelo
    """)

    equipamentos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return equipamentos