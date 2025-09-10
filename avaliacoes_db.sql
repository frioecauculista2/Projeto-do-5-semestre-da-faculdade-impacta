CREATE DATABASE avaliacoes_db;
USE avaliacoes_db;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL
);

CREATE TABLE avaliacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    produto VARCHAR(100) NOT NULL,
    nota INT NOT NULL,
    comentario TEXT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

SELECT * FROM usuarios