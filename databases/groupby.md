The GROUP BY statement groups rows that have the same values into summary rows, like "find the number of customers in each country".

Example:

```sql
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;
```