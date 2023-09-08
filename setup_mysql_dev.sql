-- Creates a databae hbnb_dev_db
-- Create a new user hbnb_dev
-- The user's password is hbnb-dev_pwd
-- The user should have all Privileges
-- hbnb_dev should have SELEC privilege on performance_scheme

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
