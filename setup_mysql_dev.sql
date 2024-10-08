-- Prepares the MySQL server for the project

-- Create the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;


-- Create a new user for the database
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';


-- Revoke all privileges for `hbnb_dev` user
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'hbnb_dev'@'localhost';


-- Grant `hbnb_dev` privileges in the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';


-- Grant SELECT privilege on database `performance_schema`
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;

