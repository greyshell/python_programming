# author: greyshell
# description: drop all tables an db
# usage: mysql -u root --password=<pass> < db_drop.sql
# lab: xss

DROP TABLE vulnapp.tbl_users;

DROP DATABASE vulnapp;