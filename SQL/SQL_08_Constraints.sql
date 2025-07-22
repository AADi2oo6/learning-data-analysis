-- MySQL Constraints
-- Constraints in MySQL are rules applied to table columns to ensure the accuracy, validity, and integrity of the data.

-- NOTE WHILE ADDING CONSTRAINTS(USING 'ADD CONSTRAINTS') ALWAYS PROVIDE A NAME AND AFTER 
-- THE TABLE ENSURE THAT THE TABLE NAME IS WRITEN IN SIDE THE BRACKET

-- 1. UNIQUE Constraint
-- Ensures that all values in a column are different.
CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);

-- Add UNIQUE using ALTER TABLE:
ALTER TABLE users              --     - this is the column name
ADD CONSTRAINT unique_email UNIQUE (email);
                --   ^ this is the name of the constarint 


-- 2. NOT NULL Constraint
-- Ensures that a column cannot contain NULL values.
ALTER TABLE users
    MODIFY COLUMN name VARCHAR(100) Not NULL;

-- 3. CHECK Constraint
-- Ensures that values in a column satisfy a specific condition.
ALTER TABLE users
    ADD CONSTRAINT dobCheck CHECK (date_Of_birth<'2005-01-01');

-- 4. DEFAULT Constraint
-- Sets a default value for a column if none is provided during insert.

CREATE TABLE users (
    id INT PRIMARY KEY,
    is_active BOOLEAN DEFAULT TRUE
);

-- Add DEFAULT using ALTER TABLE:
ALTER TABLE users
    Add column is_active BOOLEAN default TRUE;

ALTER TABLE users
ALTER COLUMN is_active SET DEFAULT FALSE;


-- Summary Table
-- Constraint	    Purpose
-- UNIQUE	        Prevents duplicate values
-- NOT NULL	        Ensures value is not NULL
-- CHECK	        Restricts values using a condition
-- DEFAULT	        Sets a default value
-- PRIMARY KEY	    Uniquely identifies each row
-- AUTO_INCREMENT	Automatically generates unique numbers