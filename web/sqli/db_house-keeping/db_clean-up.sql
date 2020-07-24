# author: greyshell
# usage: mysql -u root -p < resource.sql
# alternale usage for automation: mysql -u root --password=mypass < resource.sql

# sql injection: case02, clear the posts
delete from vulnapp.tbl_post02 where user NOT LIKE 'asinha%';

# sql injection: case03, clear the posts
delete from vulnapp.tbl_post03 where user LIKE 'anonymous-%';
update vulnapp.tbl_post03 set age = 25, comment = 'Hello', city = 'San Jose' where user = 'admin';