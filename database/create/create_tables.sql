-- User Table
CREATE TABLE User (
    username_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    user_id VARCHAR(255) -- This field is marked as FK in the diagram but not linked. It should be a PK in this table or removed if not used.
);

-- Expenses Table
CREATE TABLE Expenses (
    expences_id INT AUTO_INCREMENT PRIMARY KEY,
    amount VARCHAR(255) NOT NULL, -- Usually, the amount should be DECIMAL or FLOAT data type
    user_id VARCHAR(255),
    date DATE NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES User(username_id) -- Assuming the FK references the PK of User table
);

-- Savings Table
CREATE TABLE Savings (
    savings_id INT AUTO_INCREMENT PRIMARY KEY, -- This should be named savings_id
    amount VARCHAR(255) NOT NULL, -- Usually, the amount should be DECIMAL or FLOAT data type
    user_id VARCHAR(255),
    date DATE NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES User(username_id) -- Assuming the FK references the PK of User table
);
