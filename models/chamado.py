from database.connection import get_connection

def listar_chamados():

    conexao = get_connection()

    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
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
            
        ORDER BY c.id DESC
        
    """)

    chamados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return chamados