-- Prepare SQL server (MySQL)
-- DB name: hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creating new user named 
-- user : hbnb_dev (all privileges)
-- password : hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- privilege
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Goot to remember to flush
FLUSH PRIVILEGES;
-- grant SELECT privilege
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
--flush again
FLUSH PRIVILEGES;
