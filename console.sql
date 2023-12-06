Create database ecomon;
use ecomon;
CREATE TABLE data (
    year INT ,
    objectName VARCHAR(255) ,
    activity VARCHAR(255) ,
    location VARCHAR(255),
    no2 DECIMAL(10, 2),
    so2 DECIMAL(10, 2),
    co DECIMAL(10, 2),
    microparts DECIMAL(10, 2),
    summary DECIMAL(10, 2),
    id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE table rfc (
    id INT AUTO_INCREMENT PRIMARY KEY,
    substanceName VARCHAR(255),
    rfc_n DECIMAL(10, 2)
);

INSERT INTO rfc (substanceName, rfc_n)
VALUES
    ('NO2', 0.04),
    ('SO2', 0.08),
    ('CO', 3);

CREATE TABLE data_calculations_nkr (
    id INT AUTO_INCREMENT PRIMARY KEY,
    objectName ENUM ('ТзОВ «Птахокомплекс Губин»', 'Локачинський ЦВНТК ПАТ «Укргазвидобування»', 'ДП «Волиньторф»') ,
    substanceName ENUM ('NO2', 'SO2', 'CO'),
    concentration decimal(10,4),
    nkr decimal(10,4)
);


CREATE TABLE data_calculations_kr (
    id INT AUTO_INCREMENT PRIMARY KEY,
    objectName ENUM ('ТзОВ «Птахокомплекс Губин»', 'Локачинський ЦВНТК ПАТ «Укргазвидобування»', 'ДП «Волиньторф»') ,
    pollutantName ENUM ('NO2', 'SO2', 'CO'),
    ca decimal(10,4),
    ch decimal(10,4),
    tout decimal(10,4),
    tin decimal(10,4),
    vout decimal(10,4),
    vin decimal(10,4),
    ef decimal(10,4),
    ed decimal(10,4),
    bw decimal(10,4),
    at decimal(10,4),
    kr decimal(10,4),
    level Varchar(255)
);

drop table data;

select * from rfc;

select * from data_calculations_kr;
drop table data_calculations_nkr;
drop database ecomon;

CREATE table taxes_water (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year int,
    objectName VARCHAR(255),
    pollutant_name varchar(255),
    concentration varchar(255),
    weight float,
    tax float
);

CREATE table taxes_placement (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year int,
    objectName VARCHAR(255),
    classDanger varchar(255),
    coefDanger varchar(255),
    weight float,
    tax float
);

CREATE table taxes_radiation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year int,
    objectName VARCHAR(255),
    CategoryDanger varchar(255),
    valueElectricity float,
    tax float
);
CREATE table taxes_temporaryRadiation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year int,
    objectName VARCHAR(255),
    CategoryDanger varchar(255),
    taxRadiation float,
    valueVolume float,
    time float,
    tax float
);


CREATE TABLE LossOfLife  (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ml FLOAT,
    mt FLOAT,
    mi FLOAT,
    mz_adult FLOAT,
    mz_child FLOAT,
    num_l INT,
    num_t INT,
    num_i INT,
    num_z_adult INT,
    num_z_child INT,
    loss_rr FLOAT
);