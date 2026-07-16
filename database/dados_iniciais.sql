INSERT INTO categoria (nome, descricao)
VALUES
('Hardware', 'Problemas relacionados a equipamentos físicos'),
('Software', 'Problemas relacionados a sistemas'),
('Rede', 'Problemas relacionados à infraestrutura de rede'),
('Impressora', 'Problemas relacionados a impressoras');

INSERT INTO prioridade (nome, tempo_sla)
VALUES
('Baixa', 48),
('Média', 24),
('Alta', 8),
('Crítica', 4);

INSERT INTO usuario (nome, email, senha, telefone, departamento, perfil)
VALUES
('Caio', 'caio@ticket.com', 'Caio@1', '(11) 99354-0606', 'TI', 'Técnico'),
('Giovanna', 'giovanna.adv@ticket.com', 'Gioadv2', '(11) 94881-6688', 'Juridico', 'Usuário'),
('Rosana', 'rosana.sec@ticket.com', 'Rohsec3', '(11) 95590-0640', 'Administrativo', 'Usuário'),
('Thiago', 'tgm.dev@ticket.com', 'Devth4', '(11) 93426-3839', 'TI', 'Administrador'),
('Fabiano', 'fb.tec@ticket.com', 'Tecfb5', '(11) 98819-0132', 'TI', 'Técnico'),
('Gabriela', 'gabriela.adv@ticket.com', 'Gabadv6', '(11) 99169-0292', 'Juridico', 'Usuário');

INSERT INTO equipamento (patrimonio, fabricante, modelo, numero_serie)
VALUES
('TI0001', 'Dell', 'Latitude5420', 'DL5420A001'),
('TI0002', 'Lenovo', 'ThinkPad', 'E14LNVE14B002'),
('TI0003','Dell','OptiPlex 7090','OP7090C003'),
('TI0004', 'HP', 'LaserJet Pro M404', 'HPM404D004'),
('TI0005', 'LG', '24MK430H', 'LG24MK005'),
('TI0006','Acer', 'Aspire 5', 'ACASP5F006');

INSERT INTO chamado (titulo, descricao, usuario_id, tecnico_id, categoria_id, prioridade_id, equipamento_id)
VALUES
('Notebook', 'O notebook não liga mais.', 2, 5, 1, 3, 2),
('Impressora', 'A impressora não está fazendo compartilhamento de rede.', 6, 1, 4, 2, 4),
('Sistema', 'O sistema não está subindo', 3, 4, 2, 1, 6)


SELECT
    chamado.titulo,
    u.nome AS usuario,
    t.nome AS tecnico,
    categoria.nome AS categoria,
    prioridade.nome AS prioridade,
    equipamento.patrimonio,
    chamado.status

FROM chamado

JOIN usuario u
ON chamado.usuario_id = u.id

JOIN usuario t
ON chamado.tecnico_id = t.id

JOIN categoria
ON chamado.categoria_id = categoria.id

JOIN prioridade
ON chamado.prioridade_id = prioridade.id

JOIN equipamento
ON chamado.equipamento_id = equipamento.id;