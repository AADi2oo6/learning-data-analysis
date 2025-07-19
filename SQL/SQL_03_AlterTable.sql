-- Inserting a column to the table 
-- ALTER TABLE users ADD COLUMN is_active BOOLEAN
-- DEFAULT TRUE;


-- droping a table from the table;
-- ALTER TABLE users DROP COLUMN is_active;

-- Modefying a column
-- ALTER TABLE USERS 
-- MODIFY COLUMN name VARCHAR(130);


-- SHIFTING POSITION OF THE COLUMNS
-- ALTER TABLE USERS 
-- MODIFY COLUMN email VARCHAR(100)
-- AFTER ID;

-- SHIFTING POSITION TO 1ST POSITION
-- ALTER TABLE users
-- MODIFY COLUMN date_Of_birth DATETIME FIRST;
DESCRIBE users;