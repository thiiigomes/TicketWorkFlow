CREATE DATABASE ticket_worflow;

USE ticket_worflow;

CREATE TABLE usuario (
 
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    telfone VARCHAR(20),
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
