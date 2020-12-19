# author: greyshell
# description: truncate tables
# usage: mysql -u root --password=<pass> < db_clean.sql
# lab: sqli

# case02: clear all posts, not created by 'asinha'
DELETE FROM vulnapp.tbl_post02 WHERE user NOT LIKE 'asinha%';

# case03: clear all posts, created by default anonymous user
DELETE FROM vulnapp.tbl_post03 WHERE user LIKE 'anonymous-%';

# case03: reset to the default settings
UPDATE vulnapp.tbl_post03 SET age = 25, comment = 'Hello', city = 'San Jose' WHERE user = 'admin';