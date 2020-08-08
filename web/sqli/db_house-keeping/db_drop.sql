# author: greyshell
# usage: mysql -u root -p < resource.sql
# alternale usage for automation: mysql -u root --password=mypass < resource.sql

# drop all tables
# sql injection: case01
DROP TABLE vulnapp.tbl_post01

# sql injection: case02
DROP TABLE vulnapp.tbl_post02
DROP TABLE vulnapp.tbl_secret

# sql injection: case03
DROP TABLE vulnapp.tbl_post03

DROP DATABASE vulnapp;