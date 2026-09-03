from database.connection import get_connection


def criar_notificacao(
    usuario_id,
    chamado_id,
    mensagem
):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO notificacao (
            usuario_id,
            chamado_id,
            mensagem
        )
        VALUES (%s, %s, %s)
    """, (
        usuario_id,
        chamado_id,
        mensagem
    ))

    conexao.commit()

    cursor.close()
    conexao.close()

def listar_notificacoes(usuario_id):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            n.id,
            n.chamado_id,
            n.mensagem,
            n.lida,
            n.data_criacao
        FROM notificacao n
        WHERE n.usuario_id = %s
        ORDER BY n.data_criacao DESC
    """, (usuario_id,))

    notificacoes = cursor.fetchall()

    cursor.close()
    conexao.close()

    return notificacoes

def contar_notificacoes_nao_lidas(usuario_id):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM notificacao
        WHERE usuario_id = %s
        AND lida = FALSE
    """, (usuario_id,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado[0]

def marcar_notificacao_como_lida(
    notificacao_id,
    usuario_id
):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE notificacao
        SET lida = TRUE
        WHERE id = %s
        AND usuario_id = %s
    """, (
        notificacao_id,
        usuario_id
    ))

    conexao.commit()

    cursor.close()
    conexao.close()