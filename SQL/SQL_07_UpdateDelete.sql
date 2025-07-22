-- update: is used to modefy the existing Data;
UPDATE users 
            set  
                name = "Aditya Sharma",
                email = "adishahil346@gmail.com "
                -- date_of_birth = '2006-04-03'

            where id = 1;

-- We can also update values without using the WHERE clause but it will change all teh values 

-- DELETE : removing data from a table 

DELETE FROM users
WHERE ID = 5; --THIS WILL REMOVE THE DATA OF THE USER WHERE ID = 5
SELECT * FROM users ;

DELETE FROM users
    WHERE salary<60000 and gender = 'Female';


-- DELETE FROM users ; --Delete'S All Rows (but keep table structure)

-- DROP TABLE USERS;-- delete's the table entirly




