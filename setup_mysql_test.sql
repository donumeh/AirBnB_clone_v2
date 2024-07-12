-- Prepares the MySQL server for the project

-- Create the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;


-- Create a new user for the database
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';


-- Revoke all privileges for `hbnb_test` user
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'hbnb_test'@'localhost';


-- Grant `hbnb_test` privileges in the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';


-- Grant SELECT privilege on database `performance_schema`
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;

