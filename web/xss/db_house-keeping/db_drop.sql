# author: greyshell
# description: drop all tables an db
# usage: mysql -u root --password=<pass> < drop_tbls.sql
# lab: xss

DROP TABLE vulnapp.tbl_users;

DROP DATABASE vulnapp;