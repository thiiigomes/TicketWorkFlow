from database.connection import get_connection


def listar_usuarios():
    conexao = get_connection()

    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id,
            nome,
            email
        FROM usuario
    """)

    usuarios = cursor.fetchall()

    cursor.close()
    conexao.close()

    return usuarios

def buscar_usuario_por_email(email):
    conexao = get_connection()

    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM usuario
        WHERE email = %s
    """, (email,))

    usuario = cursor.fetchone()

    cursor.close()
    conexao.close()

    return usuario

def buscar_usuario_por_id(usuario_id):

    conexao = get_connection()

    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id,
            nome,
            email,
            perfil
        FROM usuario
        WHERE id = %s
    """, (usuario_id,))

    usuario = cursor.fetchone()

    cursor.close()
    conexao.close()

    return usuario

def listar_tecnicos():

    conexao = get_connection()

    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id,
            nome
        FROM usuario
        WHERE perfil = 'Técnico'
        ORDER BY nome
    """)

    tecnicos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return tecnicos