-- 1. Aggregate Functions
-- These return a single value from a set of rows.

-- Count total number of users:
SELECT COUNT(*) FROM users;

-- Count users who are Female:
SELECT COUNT(*) FROM users WHERE gender = 'Female';


-- use of MIN() and MAX();
SELECT MAX(salary) FROM users;

SELECT MIN(salary) as MIN_Salary , MAX(salary) as MAX_Salary FROM users;

--  use of SUM() and AVG();
SELECT sum(Salary) as TotalSalary , AVG(SALARY) AS AverageSalary FROM users;

-- 2. STRING FUNCTIONS 
-- LENGTH(); this will return the lenght of the string 
SELECT name , LENGTH(NAME) AS NameLenght from users;

-- LOWER() AND UPPER(); this will conver the name to lower or upper case;
SELECT upper(name) , email, date_Of_birth from users;

-- CONCAT() : Use to combine 2 or more stirngs
SELECT name, concat(name," <",email," >") as userName from users;

-- 3. DATE FUNCTIONS
/*
MySQL comes with the following data types for storing a date or a date/time value in the database:
    DATE - format YYYY-MM-DD
    DATETIME - format: YYYY-MM-DD HH:MI:SS
    TIMESTAMP - format: YYYY-MM-DD HH:MI:SS
    YEAR - format YYYY or YY
*/



-- NOW() : this will return current date and time;
-- CURDATE();
SELECT year(NOW());
SELECT CURdate();

-- YEAR(), MONTH(), DAY() ; this will return the parts of dat
SELECT DAY(NOW()) AS DAY, MONTH(NOW()) AS MONTH ,YEAR(NOW()) AS year;


-- DATEDIFF() : COUNTS AND RETURNS THE NUMBER OF DAYS IN BETWEEN TOW DATES
SELECT NAME, DATEDIFF(NOW(),date_Of_birth) AS DaysOld from users;

-- TIMESTAMPDIFF():CALCULATE AGE IN YEAR
SELECT NAME, TIMESTAMPDIFF(MONTH,date_Of_birth,now()) as YearOld from users;
SELECT NAME, TIMESTAMPDIFF(YEAR,date_Of_birth,now()) as YearOld from users;


-- 4. Mathematical Functions
-- ROUND(), FLOOR(), CEIL()

-- MOD() :returns the remender of two numbers;
SELECT id, mod(id,2) as remander from users;


-- 5. Conditional Functions
-- IF()

SELECT name, gender,
       IF(gender = 'Female', 'Yes', 'No') AS is_female
FROM users;
SELECT * from customer;
SELECT ContactName,city,Country ,if (country = 'UK','yes',"NO") as CitigenOfUK from customer;


/*
        Summary Table
Function 	         Purpose
COUNT() 	         Count rows
SUM() 	             Total of a column
AVG() 	             Average of values
MIN()/MAX() 	     Lowest / highest value
LENGTH() 	         String length
CONCAT() 	         Merge strings
YEAR()/DATEDIFF() 	 Date breakdown / age
ROUND() 	         Rounding numbers
IF() 	             Conditional logic
*/