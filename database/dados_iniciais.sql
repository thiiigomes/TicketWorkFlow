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
