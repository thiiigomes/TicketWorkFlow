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

INSERT INTO comentario (mensagem, usuario_id, chamado_id)
VALUES
('O notebook não liga desde o início do expediente.', 2, 1),
('Estou verificando o equipamento.', 5, 1),
('Testei outra tomada e continua sem ligar.', 2, 1),
('Identifiquei defeito na fonte. Vou providenciar a substituição.', 5, 1),

('A impressora continua offline.', 6, 2),
('Vou verificar o compartilhamento da impressora.', 1, 2),

('O sistema continua indisponível.', 3, 3),
('Servidor reiniciado. Pode testar novamente?', 4, 3),

('O sistema não abre, está offline.', 2, 4),
('Vou verificar o problema e retorno.', 4, 4),
('Sistema atualizado. Pode verificar agora?', 4, 4),

('Meu notebook está muito lento, e travando muito.', 6, 5),
('Estou verificando e seu NVME está com problema. Terá que fazer a troca do aparelho.', 5, 5),

('Meu Desktop travou, deu uma tela azul', 3, 6),
('Acabei de verificar aqui, que está com problema de memória.', 1, 6);

INSERT INTO historico (tipo_movimentacao, status_anterior, status_novo, descricao, chamado_id, usuario_id)
VALUES
('CRIAR_CHAMADO', NULL, 'Aberto', 'Giovanna criou o chamado.', 1, 2),
('ATRIBUIR_TECNICO', 'Aberto', 'Em Atendimento', 'Fabiano assumiu o chamado.', 1, 5),

('CRIAR_CHAMADO', NULL, 'Aberto', 'Gabriela criou o chamado.', 2, 6),
('ATRIBUIR_TECNICO' 'Aberto', 'Em Atendimento', 'Caio assumiu o chamado.', 2, 1),

('CRIAR_CHAMADO', NULL, 'Aberto', 'Rosana criou o chamado.', 3, 3),
('ATRIBUIR_TECNICO', 'Aberto', 'Em Atendimento', 'Thiago assumiu o chamado.', 3, 4),

('CRIAR_CHAMADO', NULL, 'Aberto', 'Giovanna criou o chamado.', 4, 2),
('ATRIBUIR_TECNICO', 'Aberto', 'Em Atendimento', 'Thiago assumiu o chamado.', 4, 4),

('CRIAR_CHAMADO', NULL, 'Aberto', 'Gabriela criou o chamado.', 5, 6),
('ATRIBUIR_TECNICO', 'Aberto', 'Em Atendimento', 'Fabiano assumiu o chamado.', 5, 5),

('CRIAR_CHAMADO', NULL, 'Aberto', 'Rosana criou o chamado', 6, 3),
('ATRIBUIR_TECNICO', 'Aberto', 'Em Atendimento', 'Caio assumiu o chamado.', 6, 1);

INSERT INTO anexo (nome_arquivo, tipo, tamanho, caminho_arquivo, comentario_id, usuario_id)
VALUES
('notebook_sem_ligar.jpg', 'jpg', '2.1 MB', 'uploads/notebook_sem_ligar.jpg', 1, 2),

('erro_sistema.png', 'png', '1.5 MB', 'uploads/erro_sistema.png', 9, 2),

('gerenciador_tarefas.png', 'png', '980 KB', 'uploads/gerenciador_tarefas.png', 12, 6),

('tela_azul.jpg', 'jpg', '3.4 MB', 'uploads/tela_azul.jpg', 14, 3);