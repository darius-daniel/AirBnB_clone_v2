-- A script that prepares a MySQL server for the project
-- This query creates a new database named hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- This query creates a new user named hbnb_test
CREATE USER IF NOT EXISTS  'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grants all all privileges on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grants select privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
