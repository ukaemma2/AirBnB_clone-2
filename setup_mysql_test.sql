-- Creates a databae hbnb_test_db
-- Create a new user hbnb_test
-- The user's password is hbnb-test_pwd
-- The user should have all Privileges
-- hbnb_test should have SELEC privilege on performance_scheme

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
