use sqltuts;
 CREATE TABLE users(
 id INT auto_increment PRIMARY KEY,
 name varchar(100) NOT NULL,
 email varchar(100) NOT NULL,
 gender ENUM('Male','Femail','Other'),
 date_Of_birth DATE,
 created_at timestamp DEFAULT current_timestamp
 );
 select * from users;