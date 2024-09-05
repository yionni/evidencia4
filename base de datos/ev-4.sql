CREATE DATABASE InyectoresDeCera;
USE InyectoresDeCera;
CREATE TABLE Inyectores (
    idInyectores INT AUTO_INCREMENT,
    modelo VARCHAR(50),
    marca VARCHAR(50),
    capacidad VARCHAR(100),
    PRIMARY KEY (idInyectores)
);
CREATE TABLE Clientes (
	IdDni INT AUTO_INCREMENT,
    telefono VARCHAR(50),
    direccion VARCHAR(50),
    mail VARCHAR(100),
    PRIMARY KEY (idDni)
);
CREATE TABLE Proveedores (
	IdProveedor INT AUTO_INCREMENT,
    telefono VARCHAR(50),
    direccion VARCHAR(50),
    mail VARCHAR(100),
    PRIMARY KEY (IdProveedor)
);
INSERT INTO Inyectores 
(idInyectores, modelo, marca, capacidad) VALUES ('0001','2.0', 'Kaya Cast', '300lt');
INSERT INTO Inyectores 
(idInyectores, modelo, marca, capacidad) VALUES ('0002','3.0', 'Memco', '250lt');
INSERT INTO Inyectores 
(idInyectores, modelo, marca, capacidad) VALUES ('0003','2.0', 'Neutec/Rio Grande', '350lt');
INSERT INTO Inyectores 
(idInyectores, modelo, marca, capacidad) VALUES ('0004','2.0', 'Yasui', '50lt');
INSERT INTO Inyectores 
(idInyectores, modelo, marca, capacidad) VALUES ('0005','4.0', 'NobleCast', '150lt');
INSERT INTO Inyectores 
(idInyectores, modelo, marca, capacidad) VALUES ('0006','1.5', 'Solidscape', '100lt');
INSERT INTO Inyectores 
(idInyectores, modelo, marca, capacidad) VALUES ('0007','3.5', 'Dolphin', '200lt');
INSERT INTO Inyectores 
(idInyectores, modelo, marca, capacidad) VALUES ('0008','4.5', 'Galloni', '250lt');
INSERT INTO Inyectores 
(idInyectores, modelo, marca, capacidad) VALUES ('0009','8.5', 'Ti Research', '150lt');
INSERT INTO Inyectores 
(idInyectores, modelo, marca, capacidad) VALUES ('0010','5.0', 'Indutherm', '50lt');

select * from Inyectores;

USE InyectoresDeCera;

select * from Inyectores;

select * from Clientes;

SELECT * FROM Proveedores;

INSERT INTO Clientes 
(IdDni, telefono, direccion, mail) VALUES ('35000000','353-484849', 'avenida siempre viva 236', 'ale@gmail.com');
INSERT INTO Proveedores 
(IdProveedor, telefono, direccion, mail) VALUES ('0001','0800-333-1111', 'avenida del trabajo 346', 'ale@gmail.com');

SELECT * FROM Proveedores;

SELECT modelo, marca FROM Inyectores;

SELECT modelo, marca from inyectores WHERE IdInyectores=0001;

SELECT marca, capacidad from inyectores WHERE IdInyectores=0002;

select capacidad from inyectores where IdInyectores=0003;
