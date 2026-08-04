from database.connection import get_connection

def listar_chamados(
    pesquisa="",
    status="",
    prioridade="",
    tecnico=""
):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT

            c.id,
            c.titulo,
            c.status,

            u.nome AS solicitante,
            t.nome AS tecnico,
            cat.nome AS categoria,
            p.nome AS prioridade,
            CONCAT(e.fabricante, ' ', e.modelo) AS equipamento

        FROM chamado c

        JOIN usuario u
            ON c.usuario_id = u.id

        JOIN usuario t
            ON c.tecnico_id = t.id

        JOIN categoria cat
            ON c.categoria_id = cat.id

        JOIN prioridade p
            ON c.prioridade_id = p.id

        JOIN equipamento e
            ON c.equipamento_id = e.id

        WHERE 1=1
    """

    parametros = []

    if pesquisa:

        sql += " AND c.titulo LIKE %s"
        parametros.append(f"%{pesquisa}%")

    if status:

        sql += " AND c.status = %s"
        parametros.append(status)

    if prioridade:

        sql += " AND p.nome = %s"
        parametros.append(prioridade)

    if tecnico:

        sql += " AND t.nome = %s"
        parametros.append(tecnico)

    sql += " ORDER BY c.id DESC"

    cursor.execute(sql, parametros)

    chamados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return chamados

def criar_chamado(
    titulo,
    descricao,
    usuario_id,
    tecnico_id,
    categoria_id,
    prioridade_id,
    equipamento_id
):
    

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO chamado (
        titulo,
        descricao,
        status,
        usuario_id,
        tecnico_id,
        categoria_id,
        prioridade_id,
        equipamento_id
    )
    VALUES (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    )
""", (
    titulo,
    descricao,
    "Aberto",
    usuario_id,
    tecnico_id,
    categoria_id,
    prioridade_id,
    equipamento_id
))

    conexao.commit()

    cursor.close()
    conexao.close()

def atualizar_chamado(
    chamado_id,
    titulo,
    descricao,
    tecnico_id,
    categoria_id,
    prioridade_id,
    equipamento_id,
    status
):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE chamado
        SET
            titulo = %s,
            descricao = %s,
            tecnico_id = %s,
            categoria_id = %s,
            prioridade_id = %s,
            equipamento_id = %s,
            status = %s
        WHERE id = %s
    """, (
        titulo,
        descricao,
        tecnico_id,
        categoria_id,
        prioridade_id,
        equipamento_id,
        status,
        chamado_id
    ))

    conexao.commit()

    cursor.close()
    conexao.close()

def buscar_chamado_por_id(chamado_id):
    
    conexao = get_connection()

    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            
            c.id,
            c.titulo,
            c.descricao,
            c.status,
           
            c.usuario_id,
            c.tecnico_id,
            c.categoria_id,
            c.prioridade_id,
            c.equipamento_id,

            c.data_abertura,
            c.data_fechamento,
            
            u.nome AS solicitante,
            t.nome AS tecnico,
            cat.nome AS categoria,
            p.nome AS prioridade,
            CONCAT(e.fabricante, ' ', e.modelo) AS equipamento
        
        FROM chamado c
        
        JOIN usuario u
            ON c.usuario_id = u.id
            
        JOIN usuario t
            ON c.tecnico_id = t.id
            
        JOIN categoria cat
            ON c.categoria_id = cat.id
        
        JOIN prioridade p
            ON c.prioridade_id = p.id
            
        JOIN equipamento e
            ON c.equipamento_id = e.id
        
        WHERE c.id = %s
    
    """, (chamado_id,))

    chamado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return chamado

def contar_chamados():

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM chamado
    """)

    total = cursor.fetchone()[0]

    cursor.close()
    conexao.close()

    return total

def contar_abertos():

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM chamado
        WHERE status = 'Aberto'
    """)

    total = cursor.fetchone()[0]

    cursor.close()
    conexao.close()

    return total


def contar_andamento():

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM chamado
        WHERE status = 'Em andamento'
    """)

    total = cursor.fetchone()[0]

    cursor.close()
    conexao.close()

    return total


def contar_fechados():

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM chamado
        WHERE status = 'Fechado'
    """)

    total = cursor.fetchone()[0]

    cursor.close()
    conexao.close()

    return total

def listar_ultimos_chamados():

    conexao = get_connection()

    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT

            c.id,
            c.titulo,
            c.status,

            t.nome AS tecnico,

            p.nome AS prioridade

        FROM chamado c

        JOIN usuario t
            ON c.tecnico_id = t.id

        JOIN prioridade p
            ON c.prioridade_id = p.id

        ORDER BY c.id DESC

        LIMIT 5
    """)

    chamados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return chamados