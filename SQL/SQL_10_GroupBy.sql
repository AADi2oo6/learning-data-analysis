-- Grouping with GROUP BY;
SELECT gender,AVG(Salary) FROM users GROUP BY gender;

SELECT COUNT(customerID), country from customer GROUP BY Country;

SELECT COUNT(customerID), country from customer
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;