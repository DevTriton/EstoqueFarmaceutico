CREATE DATABASE ESTOQUE_FARMACEUTICO;
USE ESTOQUE_FARMACEUTICO;

CREATE TABLE REMEDIOS(
	`ID_REMEDIO` INT NOT NULL auto_increment,
    `FK_DESTRIBUIDOR` INT,
	`NOME` VARCHAR(200) NOT NULL,
	`FABRICANTE` VARCHAR(200) NOT NULL,
	`DOSE` varchar(200) NOT NULL,
	`TARJA` int NOT NULL,
	`QTD_COMPRIMIDOS` INT NOT NULL,
    `DATA` DATE NOT NULL,
    `VALOR` FLOAT NOT NULL,
    `DESCRICAO` VARCHAR(255) NOT NULL,
    `QTD_REMEDIOS` INT NOT NULL,
    PRIMARY KEY (`ID_REMEDIO`),
    FOREIGN KEY (`FK_DESTRIBUIDOR`) REFERENCES DESTRIBUIDOR (`ID_DESTRIBUIDOR`)
);

CREATE TABLE ESTOQUE(
	`ID_ESTOQUE` INT NOT NULL auto_increment,
    `FK_REMEDIOS` INT,
    `FK_DESTRIBUIDOR` INT,
    PRIMARY KEY (`ID_ESTOQUE`),
    FOREIGN KEY (`FK_REMEDIOS`) REFERENCES REMEDIOS (`ID_REMEDIO`),
    FOREIGN KEY (`FK_DESTRIBUIDOR`) REFERENCES DESTRIBUIDOR (`ID_DESTRIBUIDOR`)
);

CREATE TABLE REGULAMENTACOES(
	`ID_REGULAMENTACAO` INT NOT NULL auto_increment,
	`DESCRICAO` VARCHAR(255) NOT NULL,
    Primary key(`ID_REGULAMENTACAO`)
);

CREATE TABLE FUNCIONARIO(
	`ID_FUNCIONARIO` INT NOT NULL auto_increment,
    `NOME` VARCHAR(200) NOT NULL,
    `CPF` INT NOT NULL,
    `CARGO` INT NOT NULL,
    PRIMARY KEY (`ID_FUNCIONARIO`)
);   

CREATE TABLE DESTRIBUIDOR(
	`ID_DESTRIBUIDOR` INT NOT NULL auto_increment,
	`NOME` VARCHAR(200) NOT NULL,
	`CNPJ` INT NOT NULL,
    `TEL` FLOAT NOT NULL,
    `EMAIL` VARCHAR(200) NOT NULL,
    `OBSERVACAO` VARCHAR(250) NOT NULL, 
    PRIMARY KEY (`ID_DESTRIBUIDOR`)
); 

CREATE TABLE ENDERECO(
	`ID_ENDERECO` INT NOT NULL auto_increment,
    `FK_DESTRIBUIDOR` INT,
    `RUA` VARCHAR(200),
    `CIDADE` VARCHAR(200),
    `ESTADO` VARCHAR(200),
    `NUMERO` INT,
    `CEP` INT NOT NULL,
    PRIMARY KEY (`ID_ENDERECO`),
    FOREIGN KEY (`FK_DESTRIBUIDOR`) REFERENCES DESTRIBUIDOR (`ID_DESTRIBUIDOR`)
);

select * from REMEDIOS