-- SQL script that creates a table users following these 
-- id which is integer, never null, auto increment and primary key
-- email which is string (255 characters), never null and unique
-- name which is string (255 characters)
CREATE TABLE IF NOT EXISTS users (
        id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
        email varchar(255) NOT NULL UNIQUE,
        name varchar(255)
);
