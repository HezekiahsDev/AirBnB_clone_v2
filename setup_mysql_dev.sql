-- Prepare SQL server (MySQL)
-- DB name: hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creating new user named 
-- user : hbnb_dev (all privileges)
-- password : hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Goot to remember to flush
FLUSH PRIVILEGES;
-- grant SELECT privilege
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
--flush again
FLUSH PRIVILEGES;
