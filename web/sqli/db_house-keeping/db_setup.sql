# author: greyshell
# description: create db, tables and inset data
# usage: mysql -u root --password=<pass> < db_setup.sql
# lab: sqli


CREATE DATABASE IF NOT EXISTS vulnapp;

# case01:
CREATE TABLE IF NOT EXISTS vulnapp.tbl_post01 (
comment VARCHAR(30) NOT NULL,
user VARCHAR(10) NOT NULL
);

INSERT INTO vulnapp.tbl_post01 (comment, user) VALUES ('hola', 'pedro');
INSERT INTO vulnapp.tbl_post01 (comment, user) VALUES ('hi', 'usman');
INSERT INTO vulnapp.tbl_post01 (comment, user) VALUES ('ola', 'amol');


# case02:
CREATE TABLE IF NOT EXISTS vulnapp.tbl_post02 (
comment VARCHAR(30) NOT NULL,
pin INT NOT NULL,
age INT NOT NULL,
user VARCHAR(30) NOT NULL
);

INSERT INTO vulnapp.tbl_post02 (comment, pin, age, user) VALUES ('hola', 100, 25, 'dhaval');

CREATE TABLE IF NOT EXISTS vulnapp.tbl_secret (
user VARCHAR(30) NOT NULL,
token INT NOT NULL,
password VARCHAR(30) NOT NULL
);

INSERT INTO vulnapp.tbl_secret (user, token, password) VALUES ('asinha', 777, 'blue@123');
INSERT INTO vulnapp.tbl_secret (user, token, password) VALUES ('admin', 101, 'grey@321');

# case03:
CREATE TABLE IF NOT EXISTS vulnapp.tbl_post03 (
comment VARCHAR(30) NOT NULL,
city VARCHAR(30) NOT NULL,
age INT NOT NULL,
user VARCHAR(30) NOT NULL,
PRIMARY KEY (user)
);

INSERT INTO vulnapp.tbl_post03 (comment, city, age, user) VALUES ('hello', 'mountain view', 25, 'dhaval');
INSERT INTO vulnapp.tbl_post03 (comment, city, age, user) VALUES ('hi', 'santa clara', 19, 'admin');
