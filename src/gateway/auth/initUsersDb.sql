-- CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Auth123';

-- CREATE DATABASE tododb;

-- GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

-- USE tododb;

CREATE TABLE IF NOT EXISTS todoUsers(
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);


-- INSERT INTO user (email, password) VALUES ('insten490@gmail.com', 'Admin123');