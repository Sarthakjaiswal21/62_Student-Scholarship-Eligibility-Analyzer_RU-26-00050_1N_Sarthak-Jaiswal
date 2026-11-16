# Project Report: Student Scholarship Eligibility Analyzer

## Objective

The objective of this project is to analyse student records and identify scholarship eligibility using marks, annual family income and attendance. The program also calculates scholarship totals and filters students based on marks.

## Problem statement

Student information is stored in a CSV file. The program reads the records, validates the values and applies the scholarship conditions given in Project No. 62.

## Eligibility and scholarship conditions

A student is eligible only when marks are 75% or above, attendance is 75% or above, and annual family income is Rs. 5,00,000 or below.

An eligible student receives a full scholarship of Rs. 50,000 when marks are at least 90% and income is at most Rs. 3,00,000. Other eligible students receive a partial scholarship of Rs. 25,000. Students who do not meet the eligibility conditions are marked Not Eligible.

## Tools and concepts

- Python 3
- Pandas
- CSV file handling
- Conditional statements and functions
- Data filtering and aggregation
- Input validation

## Program features

1. Reads student records from `students.csv`.
2. Skips records with missing or invalid values and displays a reason.
3. Checks scholarship eligibility.
4. Displays a summary of scholarship counts, total amount and average eligible marks.
5. Filters student records by a user-entered minimum marks value.

## Testing

The supplied sample data was checked against the normal input case. The expected results are:

| Student | Result |
|---|---|
| Aman | Full scholarship — Rs. 50,000 |
| Riya | Partial scholarship — Rs. 25,000 |
| Karan | Not Eligible |
| Neha | Not Eligible |

The summary for this data is 2 eligible students, 2 not eligible students, 1 full scholarship, 1 partial scholarship, total scholarship amount Rs. 75,000 and average eligible marks 86.00.

The boundary case can be checked using Ravi (90 marks, Rs. 3,00,000 income, 75% attendance) and Sita (75 marks, Rs. 5,00,000 income, 75% attendance). Ravi qualifies for a full scholarship and Sita qualifies for a partial scholarship.

The invalid-input case can be checked by entering `Amit,abc,250000,80` in the CSV. The program reports invalid marks and skips that record.

## Conclusion

The project demonstrates how Python and Pandas can be used to read, validate, filter and summarize student data. The menu makes the program easy to run from the console.
