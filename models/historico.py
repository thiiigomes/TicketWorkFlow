from database.connection import get_connection


def registrar_historico(
    chamado_id,
    usuario_id,
    acao,
    descricao=""
):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO historico_chamado (
            chamado_id,
            usuario_id,
            acao,
            descricao
        )
        VALUES (
            %s,
            %s,
            %s,
            %s
        )
    """, (
        chamado_id,
        usuario_id,
        acao,
        descricao
    ))

    conexao.commit()

    cursor.close()
    conexao.close()


def listar_historico_chamado(chamado_id):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            h.id,
            h.chamado_id,
            h.acao,
            h.descricao,
            h.data_registro,
            u.nome AS usuario

        FROM historico_chamado h

        JOIN usuario u
            ON h.usuario_id = u.id

        WHERE h.chamado_id = %s

        ORDER BY h.data_registro DESC
    """, (chamado_id,))

    historico = cursor.fetchall()

    cursor.close()
    conexao.close()

    return historico