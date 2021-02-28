THE ORDER BY statement is used to sort the results into ascending or descending order.

```sql
SELECT field1, field2
FROM tablename
ORDER BY field1 ASC/DESC;
```

Example:

```sql
SELECT * FROM Customers
ORDER BY Country DESC;
```

For numbers, ascending and descending works as expected.

For strings, it sorts alphabetically.

For dates, it sorts chronologically as long as the date format is `YYYY/MM/DD`.
