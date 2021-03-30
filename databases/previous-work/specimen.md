Database file - [DoctorsSurgery.db](DoctorsSurgery.db)

1c(i)

The surgery wants to create a list of drugIDs showing how many times each drugID is prescribed. The list should be sorted from the most prescribed drug to the least.

Implement the SQL statement that will produce this output.

```sql
SELECT Drug.drugID, COUNT(PrescribedDrug.drugID)
FROM Drug, PrescribedDrug
WHERE Drug.drugID == PrescribedDrug.drugID
GROUP BY PrescribedDrug.drugID
ORDER BY COUNT(PrescribedDrug.drugID) DESC;
```

1c(ii)

The surgery wants to identify a list of patients who have been prescribed the drug with the highest dosage.

The output should include the patientID and the datePrescribed fields, as shown below.

| patientID | datePrescribed |
| --------- | -------------- |
| 75        | 14/05/2018     |
| 88        | 14/05/2018     |
| 92        | 10/05/2018     |
| ...       | ...            |

Implement two SQL statements that will produce this output.

Subquery:

```sql
SELECT MAX(dosage) FROM Drug;
```

Full query:

```sql
SELECT PrescribedDrug.patientID, PrescribedDrug.datePrescribed
FROM PrescribedDrug, Drug
WHERE PrescribedDrug.drugID == Drug.drugID
AND Drug.dosage == (SELECT MAX(dosage) FROM Drug);
```
