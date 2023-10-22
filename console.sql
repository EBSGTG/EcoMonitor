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
CREATE TABLE data_calculations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT ,
    objectName VARCHAR(255) ,
    no2 DECIMAL(10, 2),
    so2 DECIMAL(10, 2),
    co DECIMAL(10, 2),
    no2_kr DECIMAL(10, 2),
    so2_kr DECIMAL(10, 2),
    co_kr DECIMAL(10, 2),
    no2_nkr DECIMAL(10, 2),
    so2_nkr DECIMAL(10, 2),
    co_nkr DECIMAL(10, 2)
);


select * from data;
drop table data;