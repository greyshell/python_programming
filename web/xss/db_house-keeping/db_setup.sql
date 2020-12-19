# author: greyshell
# description: create db, tables and inset data
# usage: mysql -u root --password=<pass> < db_setup.sql
# lab: xss


CREATE DATABASE IF NOT EXISTS vulnapp;

CREATE TABLE IF NOT EXISTS vulnapp.tbl_users (
id INT(11) NOT NULL AUTO_INCREMENT,
username VARCHAR(25) NOT NULL,
password VARCHAR(25) NOT NULL,
name VARCHAR(25) NOT NULL,
age INT(11) NOT NULL,
PRIMARY KEY (id)
);

INSERT INTO vulnapp.tbl_users (username, password, name, age) VALUES ('admin', 'abc', 'admin', 38);
INSERT INTO vulnapp.tbl_users (username, password, name, age) VALUES ('vampire', 'xyz', 'dhaval', 22);
