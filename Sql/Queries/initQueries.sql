## Create db
CREATE DATABASE fake_account_db;

## Create fake_account table
CREATE TABLE fake_account_db.fake_accounts (
    id INT(6) unsigned auto_increment PRIMARY KEY,
    Name VARCHAR(30),
    Address VARCHAR(30),
    Password VARCHAR(30),
    Created VARCHAR(30)
);

## Create remote user
CREATE USER 'remote'@'localhost' IDENTIFIED BY 'remote';
CREATE USER 'remote'@'%' IDENTIFIED BY 'remote';

## Grant privileges to remote user
GRANT ALL ON *.* TO 'remote'@'localhost';
GRANT ALL ON *.* TO 'remote'@'%';
flush privileges;