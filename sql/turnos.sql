CREATE DATABASE turnos_db;
USE turnos_db;

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE turno (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME NOT NULL,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);
