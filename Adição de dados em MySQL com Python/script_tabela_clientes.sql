CREATE DATABASE Cadastro
DEFAULT CHARACTER SET utf8
DEFAULT COLLATE utf8_general_ci;

USE Cadastro;

CREATE TABLE `CLIENTES` (
	ID int NOT NULL AUTO_INCREMENT,
	`NOME` varchar(30) NOT NULL,
	`EMAIL` varchar(30) NOT NULL,
	FONE double NOT NULL,
	PRIMARY KEY (ID)
) DEFAULT CHARSET = utf8;

DESC CLIENTES;
