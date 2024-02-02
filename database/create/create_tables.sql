
-- User Table
CREATE TABLE User (
    username_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE
    -- Removed the ambiguous user_id field.
);

-- Expenses Table
CREATE TABLE Expenses (
    expenses_id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL, 
    user_id INT, 
    date DATE NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES User(username_id)
);

-- Savings Table
CREATE TABLE Savings (
    savings_id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL, 
    user_id INT, 
    date DATE NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES User(username_id)
);



-- -- User Table
-- CREATE TABLE User (
--     username_id INT AUTO_INCREMENT PRIMARY KEY,
--     email VARCHAR(255) NOT NULL UNIQUE,
--     password VARCHAR(255) NOT NULL,
--     username VARCHAR(255) NOT NULL UNIQUE
--     -- Removed the ambiguous user_id field.
-- );

-- -- Expenses Table
-- CREATE TABLE Expenses (
--     expenses_id INT AUTO_INCREMENT PRIMARY KEY,
--     amount DECIMAL(10, 2) NOT NULL, -- Changed from VARCHAR to DECIMAL for monetary values.
--     user_id INT, -- Changed from VARCHAR to INT to match the User table's PK type.
--     date DATE NOT NULL,
--     description VARCHAR(255),
--     FOREIGN KEY (user_id) REFERENCES User(username_id) -- Foreign key correctly referencing the PK of User table.
-- );

-- -- Savings Table
-- CREATE TABLE Savings (
--     savings_id INT AUTO_INCREMENT PRIMARY KEY,
--     amount DECIMAL(10, 2) NOT NULL, -- Changed from VARCHAR to DECIMAL for monetary values.
--     user_id INT, -- Changed from VARCHAR to INT to match the User table's PK type.
--     date DATE NOT NULL,
--     description VARCHAR(255),
--     FOREIGN KEY (user_id) REFERENCES User(username_id) -- Foreign key correctly referencing the PK of User table.
-- );
