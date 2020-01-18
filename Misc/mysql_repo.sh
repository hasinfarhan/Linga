#Start Stop
sudo service mysql start
sudo service mysql stop

#setup permision and password for root:
sudo mysql -u root -p
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'new_pass';

#login as root
mysql -u root -p
password: new_pass


SHOW databases;
CREATE DATABASE dbname;
USE dbname;
SHOW tables;


killing tcp : sudo fuser -k 8000/tcp
