from database.connection import get_connection

def listar_chamados(
    pesquisa="",
    status="",
    prioridade="",
    tecnico="",
    usuario_id=None,
    perfil=None
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
        LEFT JOIN usuario t
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

    # Usuário comum só pode visualizar seus próprios chamados
    if perfil == "Usuário":
        sql += " AND c.usuario_id = %s"
        parametros.append(usuario_id)

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

def listar_ultimos_chamados(limite=5):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            c.id,
            c.titulo,
            c.status,
            p.nome AS prioridade,
            t.nome AS tecnico

        FROM chamado c

        JOIN prioridade p
            ON c.prioridade_id = p.id

        LEFT JOIN usuario t
            ON c.tecnico_id = t.id

        ORDER BY c.id DESC

        LIMIT %s
    """, (limite,))

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

    chamado_id = cursor.lastrowid

    cursor.close()
    conexao.close()

    return chamado_id

def atualizar_chamado(
    chamado_id,
    titulo,
    descricao,
    tecnico_id,
    categoria_id,
    prioridade_id,
    equipamento_id,
    status,
    usuario_id
):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    # Busca os dados atuais do chamado
    cursor.execute("""
        SELECT
            c.titulo,
            c.descricao,
            c.tecnico_id,
            c.categoria_id,
            c.prioridade_id,
            c.equipamento_id,
            c.status,
            c.data_fechamento,

            t.nome AS tecnico,
            cat.nome AS categoria,
            p.nome AS prioridade,
            CONCAT(e.fabricante, ' ', e.modelo) AS equipamento

        FROM chamado c

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

    chamado_atual = cursor.fetchone()

    if not chamado_atual:
        cursor.close()
        conexao.close()
        return

    # Regra de fluxo:
    # Um chamado Aberto não pode ser fechado diretamente.

    if chamado_atual["status"] == "Aberto" and status == "Fechado":

        cursor.close()
        conexao.close()

        return False

    alteracoes = []
    
    # Título
    if chamado_atual["titulo"] != titulo:

        alteracoes.append(
            f'Título: "{chamado_atual["titulo"]}" → "{titulo}"'
        )

    # Descrição
    if chamado_atual["descricao"] != descricao:

        alteracoes.append(
            "Descrição: alterada"
        )

    # Técnico
    if chamado_atual["tecnico_id"] != int(tecnico_id):

        cursor.execute("""
            SELECT nome
            FROM usuario
            WHERE id = %s
        """, (tecnico_id,))

        novo_tecnico = cursor.fetchone()

        if novo_tecnico:

            alteracoes.append(
                f'Técnico: "{chamado_atual["tecnico"]}" → '
                f'"{novo_tecnico["nome"]}"'
            )

    # Categoria
    if chamado_atual["categoria_id"] != int(categoria_id):

        cursor.execute("""
            SELECT nome
            FROM categoria
            WHERE id = %s
        """, (categoria_id,))

        nova_categoria = cursor.fetchone()

        if nova_categoria:

            alteracoes.append(
                f'Categoria: "{chamado_atual["categoria"]}" → '
                f'"{nova_categoria["nome"]}"'
            )

    # Prioridade
    if chamado_atual["prioridade_id"] != int(prioridade_id):

        cursor.execute("""
            SELECT nome
            FROM prioridade
            WHERE id = %s
        """, (prioridade_id,))

        nova_prioridade = cursor.fetchone()

        if nova_prioridade:

            alteracoes.append(
                f'Prioridade: "{chamado_atual["prioridade"]}" → '
                f'"{nova_prioridade["nome"]}"'
            )

    # Equipamento
    if chamado_atual["equipamento_id"] != int(equipamento_id):

        cursor.execute("""
            SELECT CONCAT(fabricante, ' ', modelo) AS equipamento
            FROM equipamento
            WHERE id = %s
        """, (equipamento_id,))

        novo_equipamento = cursor.fetchone()

        if novo_equipamento:

            alteracoes.append(
                f'Equipamento: "{chamado_atual["equipamento"]}" → '
                f'"{novo_equipamento["equipamento"]}"'
            )

    # Status
    if chamado_atual["status"] != status:

        alteracoes.append(
            f'Status: "{chamado_atual["status"]}" → "{status}"'
        )

    # Define a data de fechamento
    if status == "Fechado":

        data_fechamento_sql = "NOW()"

    else:

        data_fechamento_sql = "NULL"

    # Atualiza o chamado
    cursor.execute(f"""
        UPDATE chamado
        SET
            titulo = %s,
            descricao = %s,
            tecnico_id = %s,
            categoria_id = %s,
            prioridade_id = %s,
            equipamento_id = %s,
            status = %s,
            data_fechamento = {data_fechamento_sql}
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

    # Registra as alterações no histórico
    if alteracoes:

        from models.historico import registrar_historico

        descricao_historico = "\n".join(alteracoes)

        registrar_historico(
            chamado_id,
            usuario_id,
            "Chamado atualizado",
            descricao_historico
        )

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

def excluir_chamado(chamado_id):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM chamado
        WHERE id = %s
    """, (chamado_id,))

    conexao.commit()

    cursor.close()
    conexao.close()

def assumir_chamado(chamado_id, tecnico_id, usuario_id):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    # Busca o chamado atual
    cursor.execute("""
        SELECT
            c.status,
            c.tecnico_id,
            c.usuario_id,
            t.nome AS tecnico

        FROM chamado c

        LEFT JOIN usuario t
            ON c.tecnico_id = t.id

        WHERE c.id = %s
    """, (chamado_id,))

    chamado = cursor.fetchone()

    if not chamado:
        cursor.close()
        conexao.close()
        return False

    # Só chamados abertos podem ser assumidos
    if chamado["status"] != "Aberto":
        cursor.close()
        conexao.close()
        return False

    # Busca o técnico que está assumindo
    cursor.execute("""
        SELECT nome
        FROM usuario
        WHERE id = %s
    """, (tecnico_id,))

    tecnico = cursor.fetchone()

    if not tecnico:
        cursor.close()
        conexao.close()
        return False

    # Atribui o chamado ao técnico e muda o status
    cursor.execute("""
        UPDATE chamado
        SET
            tecnico_id = %s,
            status = 'Em andamento'
        WHERE id = %s
    """, (
        tecnico_id,
        chamado_id
    ))

    conexao.commit()

    cursor.close()
    conexao.close()

    # Registra no histórico

    from models.historico import registrar_historico
    from models.notificacao import criar_notificacao

    descricao = (
        f"Chamado assumido pelo técnico "
        f'"{tecnico["nome"]}". '
        f'Status: "Aberto" → "Em andamento".'
    )

    registrar_historico(
        chamado_id,
        usuario_id,
        "Chamado assumido",
        descricao
    )

    # Notifica o solicitante

    criar_notificacao(
        chamado["usuario_id"],
        chamado_id,
        f"O chamado #{chamado_id} foi assumido pelo técnico "
        f'"{tecnico["nome"]}" e está em andamento.'
    )

    return True

def transferir_chamado(
    chamado_id,
    novo_tecnico_id,
    usuario_id,
    motivo
):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    # Busca o chamado atual
    cursor.execute("""
        SELECT
            c.status,
            c.tecnico_id,
            t.nome AS tecnico_atual

        FROM chamado c

        LEFT JOIN usuario t
            ON c.tecnico_id = t.id

        WHERE c.id = %s
    """, (chamado_id,))

    chamado = cursor.fetchone()

    if not chamado:
        cursor.close()
        conexao.close()
        return False

    # O chamado precisa estar em andamento
    if chamado["status"] != "Em andamento":
        cursor.close()
        conexao.close()
        return False

    # Não pode transferir para o mesmo técnico
    if chamado["tecnico_id"] == int(novo_tecnico_id):
        cursor.close()
        conexao.close()
        return False

    # Busca o novo técnico
    cursor.execute("""
        SELECT
            id,
            nome
        FROM usuario
        WHERE id = %s
        AND perfil = 'Técnico'
    """, (novo_tecnico_id,))

    novo_tecnico = cursor.fetchone()

    if not novo_tecnico:
        cursor.close()
        conexao.close()
        return False

    # Atualiza o responsável
    cursor.execute("""
        UPDATE chamado
        SET tecnico_id = %s
        WHERE id = %s
    """, (
        novo_tecnico_id,
        chamado_id
    ))

    conexao.commit()

    cursor.close()
    conexao.close()

    # Registra no histórico
    from models.historico import registrar_historico

    descricao = (
        f"Chamado transferido de "
        f'"{chamado["tecnico_atual"]}" para '
        f'"{novo_tecnico["nome"]}". '
        f"Motivo: {motivo}"
    )

    registrar_historico(
    chamado_id,
    usuario_id,
    "Chamado transferido",
    descricao
    )

    # Cria uma notificação para o novo técnico responsável
    from models.notificacao import criar_notificacao

    criar_notificacao(
    novo_tecnico_id,
    chamado_id,
    f"O chamado #{chamado_id} foi transferido para você. "
    f"Motivo: {motivo}"
    )

    return True

def fechar_chamado(
    chamado_id,
    usuario_id,
    solucao
):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id,
            status,
            usuario_id
        FROM chamado
        WHERE id = %s
    """, (chamado_id,))

    chamado = cursor.fetchone()

    if not chamado:
        cursor.close()
        conexao.close()
        return False

    # Só pode fechar chamados em andamento
    if chamado["status"] != "Em andamento":
        cursor.close()
        conexao.close()
        return False

    # A solução é obrigatória
    if not solucao or not solucao.strip():
        cursor.close()
        conexao.close()
        return False

    cursor.execute("""
        UPDATE chamado
        SET
            status = 'Fechado',
            data_fechamento = NOW()
        WHERE id = %s
    """, (chamado_id,))

    conexao.commit()

    cursor.close()
    conexao.close()

    # Registra a solução no histórico
    from models.historico import registrar_historico
    from models.notificacao import criar_notificacao

    registrar_historico(
        chamado_id,
        usuario_id,
        "Chamado fechado",
        f"Solução registrada: {solucao.strip()}"
    )

    # Cria uma notificação para o solicitante
    criar_notificacao(
        chamado["usuario_id"],
        chamado_id,
        f"O chamado #{chamado_id} foi fechado. "
        f"Solução: {solucao.strip()}"
    )

    return True

def reabrir_chamado(chamado_id, usuario_id, motivo):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id,
            status,
            tecnico_id
        FROM chamado
        WHERE id = %s
    """, (chamado_id,))

    chamado = cursor.fetchone()

    if not chamado:
        cursor.close()
        conexao.close()
        return False

    # Só pode reabrir chamados fechados
    if chamado["status"] != "Fechado":
        cursor.close()
        conexao.close()
        return False

    # O motivo é obrigatório
    if not motivo or not motivo.strip():
        cursor.close()
        conexao.close()
        return False

    cursor.execute("""
        UPDATE chamado
        SET
            status = 'Em andamento',
            data_fechamento = NULL
        WHERE id = %s
    """, (chamado_id,))

    conexao.commit()

    cursor.close()
    conexao.close()

    from models.historico import registrar_historico
    from models.notificacao import criar_notificacao

    registrar_historico(
        chamado_id,
        usuario_id,
        "Chamado reaberto",
        f"Motivo da reabertura: {motivo.strip()}"
    )

    # Cria notificação para o técnico responsável
    if chamado["tecnico_id"]:

        criar_notificacao(
            chamado["tecnico_id"],
            chamado_id,
            f"O chamado #{chamado_id} foi reaberto. "
            f"Motivo: {motivo.strip()}"
        )

    return True

def contar_por_prioridade():

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            p.nome AS prioridade,
            COUNT(c.id) AS total
        FROM prioridade p
        LEFT JOIN chamado c
            ON c.prioridade_id = p.id
        WHERE p.nome IN ('Alta', 'Média', 'Baixa')
        GROUP BY p.nome
        ORDER BY
            CASE p.nome
                WHEN 'Alta' THEN 1
                WHEN 'Média' THEN 2
                WHEN 'Baixa' THEN 3
            END
    """)

    prioridades = cursor.fetchall()

    cursor.close()
    conexao.close()

    return prioridades