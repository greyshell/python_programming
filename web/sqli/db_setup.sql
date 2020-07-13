# author: greyshell
# usage: mysql -u root -p < resource.sql

CREATE TABLE tbl_post01 (
user_comment VARCHAR(30) NOT NULL,
user_name VARCHAR(10) NOT NULL
);

INSERT INTO tbl_post01 (user_comment, user_name) VALUES ('hola', 'pedro');
INSERT INTO tbl_post01 (user_comment, user_name) VALUES ('hello', 'jack');
INSERT INTO tbl_post01 (user_comment, user_name) VALUES ('ola', 'andre');
INSERT INTO tbl_post01 (user_comment, user_name) VALUES ('hi', 'amit');
INSERT INTO tbl_post01 (user_comment, user_name) VALUES ('salut', 'chen');


CREATE TABLE tbl_post02 (
comment VARCHAR(30) NOT NULL,
pin INT NOT NULL,
age INT NOT NULL,
user VARCHAR(30) NOT NULL
);


INSERT INTO tbl_post02 (comment, pin, age, user) VALUES ('hola', 100, 25, 'dhaval');

delete from tbl_post02 where user LIKE = 'anonymous%'
delete from tbl_post02 where pin = 0

CREATE TABLE tbl_secret (
user VARCHAR(30) NOT NULL,
token INT NOT NULL,
password VARCHAR(30) NOT NULL
);

INSERT INTO tbl_secret (user, token, password) VALUES ('dhaval', 777, 'abc');
INSERT INTO tbl_secret (user, token, password) VALUES ('ravi', 101, 'xyz');

CREATE TABLE tbl_post03 (
comment VARCHAR(30) NOT NULL,
city VARCHAR(30) NOT NULL,
age INT NOT NULL,
user VARCHAR(30) NOT NULL,
PRIMARY KEY (user)
);

INSERT INTO tbl_post03 (comment, city, age, user) VALUES ('hola', 'mountain view', 25, 'dhaval');
INSERT INTO tbl_post03 (comment, city, age, user) VALUES ('hi', 'santa clara', 37, 'admin');



