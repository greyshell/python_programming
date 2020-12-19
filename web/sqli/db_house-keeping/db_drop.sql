# author: greyshell
# description: drop all tables and db
# usage: mysql -u root --password=<pass> < db_drop.sql
# lab: sqli


# case01:
DROP TABLE vulnapp.tbl_post01

# case02:
DROP TABLE vulnapp.tbl_post02
DROP TABLE vulnapp.tbl_secret

# case03:
DROP TABLE vulnapp.tbl_post03

DROP DATABASE vulnapp;