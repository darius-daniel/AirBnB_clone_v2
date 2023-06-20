-- A script that prepares a MySQL server for the project
-- This query creates a new database named hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- This query creates a new user named hbnb_dev
CREATE USER IF NOT EXISTS  'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grants all all privileges on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grants select privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
