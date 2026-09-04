from database.connection import get_connection


def criar_comentario(chamado_id, usuario_id, mensagem):

    if not mensagem or not mensagem.strip():
        return False

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO comentario (
            mensagem,
            chamado_id,
            usuario_id
        )
        VALUES (%s, %s, %s)
    """, (
        mensagem.strip(),
        chamado_id,
        usuario_id
    ))

    conexao.commit()

    cursor.close()
    conexao.close()

    return True


def listar_comentarios(chamado_id):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            c.id,
            c.mensagem,
            c.data_hora,
            c.chamado_id,
            c.usuario_id,
            u.nome AS usuario
        FROM comentario c
        JOIN usuario u
            ON c.usuario_id = u.id
        WHERE c.chamado_id = %s
        ORDER BY c.data_hora ASC
    """, (chamado_id,))

    comentarios = cursor.fetchall()

    cursor.close()
    conexao.close()

    return comentarios