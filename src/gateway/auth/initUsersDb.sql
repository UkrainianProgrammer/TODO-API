CREATE DATABASE IF NOT EXISTS tododb;

USE tododb;

CREATE TABLE IF NOT EXISTS todoUsers(
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- INSERT INTO user (email, password) VALUES ('insten490@gmail.com', 'Admin123');