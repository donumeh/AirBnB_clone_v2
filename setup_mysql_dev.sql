-- Prepares the MySQL server for the project

-- Create the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;


-- Create a new user for the database
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';


-- Grant `hbnb_dev` privileges in the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- Grant SELECT privilege on database `performance_schema`
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

