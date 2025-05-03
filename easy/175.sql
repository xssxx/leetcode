-- 2019.04.17

SELECT FirstName, LastName, City, State 
FROM Person LEFT JOIN Address
ON Person.PersonId = Address.PersonId;