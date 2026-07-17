CREATE DATABASE ticket_workflow;

USE ticket_workflow;

CREATE TABLE usuario (
 
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    telefone VARCHAR(20),
    departamento VARCHAR(100) NOT NULL,
    perfil VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Ativo',
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categoria (

    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(255) NOT NULL
);

CREATE TABLE prioridade (

    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(10) NOT NULL,
    tempo_sla INT NOT NULL
);

CREATE TABLE equipamento (

    id INT PRIMARY KEY AUTO_INCREMENT,
    patrimonio VARCHAR(50) NOT NULL UNIQUE,
    modelo VARCHAR (100) NOT NULL,
    fabricante VARCHAR(100) NOT NULL,
    numero_serie VARCHAR(100) NOT NULL UNIQUE,
    status VARCHAR(20) NOT NULL DEFAULT 'Ativo'
);

CREATE TABLE chamado (

    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    data_abertura DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_fechamento DATETIME,
    status VARCHAR(20) NOT NULL DEFAULT 'Aberto',
    usuario_id INT NOT NULL,
    tecnico_id INT NOT NULL,
    categoria_id INT NOT NULL,
    prioridade_id INT NOT NULL,
    equipamento_id INT NOT NULL,

    FOREIGN KEY (usuario_id)
        REFERENCES usuario(id),

    FOREIGN KEY (tecnico_id)
        REFERENCES usuario(id),
    
    FOREIGN KEY (categoria_id)
        REFERENCES categoria(id),
    
    FOREIGN KEY (prioridade_id)
        REFERENCES prioridade(id),
    
    FOREIGN KEY (equipamento_id)
        REFERENCES equipamento(id)
);

CREATE TABLE comentario (

    id INT PRIMARY KEY AUTO_INCREMENT,
    mensagem TEXT NOT NULL,
    data_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    chamado_id INT NOT NULL,
    usuario_id INT NOT NULL,

    FOREIGN KEY (chamado_id)
       REFERENCES chamado(id),

    FOREIGN KEY (usuario_id)
        REFERENCES usuario(id) 
);

CREATE TABLE historico (

    id INT PRIMARY KEY AUTO_INCREMENT,
    tipo_movimentacao VARCHAR(50) NOT NULL,
    status_anterior VARCHAR(20),
    status_novo VARCHAR(20),
    descricao TEXT NOT NULL,
    data_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    chamado_id INT NOT NULL,
    usuario_id INT NOT NULL,

    FOREIGN KEY (chamado_id)
        REFERENCES chamado(id),
    
    FOREIGN KEY (usuario_id)
        REFERENCES usuario(id)
);

CREATE TABLE anexo (

    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_arquivo VARCHAR(255) NOT NULL,
    tipo VARCHAR(100) NOT NULL,
    tamanho VARCHAR(20) NOT NULL,
    caminho_arquivo VARCHAR(1000) NOT NULL,
    data_upload DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    comentario_id INT NOT NULL,
    usuario_id INT NOT NULL,

    FOREIGN KEY (comentario_id)
        REFERENCES comentario(id)

    FOREIGN KEY (usuario_id)
        REFERENCES usuario(id)
);
