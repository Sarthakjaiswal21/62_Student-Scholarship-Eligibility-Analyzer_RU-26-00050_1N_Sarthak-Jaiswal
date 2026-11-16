# Student Scholarship Eligibility Analyzer

**Project number:** 62  
**Course:** B.Tech CSE, First Semester  
**Language:** Python 3  
**Library:** Pandas

## 1. Project overview

This console-based program reads student details from a CSV file and checks scholarship eligibility using marks, family income and attendance. It can also display a summary and filter students by minimum marks.

## 2. Scholarship rules

A student is eligible when all three conditions are true:

- Marks are at least 75%.
- Attendance is at least 75%.
- Annual family income is at most Rs. 5,00,000.

For an eligible student:

- **Full scholarship (Rs. 50,000):** marks are at least 90% and income is at most Rs. 3,00,000.
- **Partial scholarship (Rs. 25,000):** eligible, but the full-scholarship conditions are not both met.

Otherwise, the student is **Not Eligible**.

## 3. Files in this project

- `main.py` — complete Python program.
- `students.csv` — sample input data for the test cases.
- `requirements.txt` — required Python library.
- `PROJECT_REPORT.md` — short project documentation.

## 4. Requirements and setup

Install Python 3. Then open a terminal in this project folder and run:

```bash
python -m pip install -r requirements.txt
python main.py
```

If your system uses the `python3` command, use `python3` instead of `python`.

## 5. Menu options

1. Check scholarship eligibility for every valid student.
2. Show eligible/not-eligible counts, full/partial counts, total scholarship amount and average marks of eligible students.
3. Filter all valid student records by a minimum marks value. This option is based on marks and does not apply the scholarship eligibility filter.
4. Exit.

## 6. Sample data and expected checks

The included CSV contains the Normal Input data from the project description.

### Option 1

```text
Aman | Full | Rs. 50000
Riya | Partial | Rs. 25000
Karan | Not Eligible
Neha | Not Eligible
```

### Option 2

```text
Eligible: 2 | Not Eligible: 2 | Full: 1 | Partial: 1
Total scholarship: Rs. 75000 | Average marks (eligible): 86.00
```

### Option 3

Enter `85`:

```text
Aman | 92
Neha | 88
```

## 7. Invalid data handling

The program skips a row if its name, marks, income or attendance is missing or invalid. It prints a message explaining why the row was skipped. Marks and attendance must be between 0 and 100; income cannot be negative.

## 8. Concepts used

- Reading CSV data with Pandas
- Functions and conditional statements
- Row-wise processing with `DataFrame.apply()`
- Filtering rows with Pandas
- Aggregation using `count`, `sum` and `mean`
- Input validation and exception handling

## 9. Test the invalid-input case

To check the invalid marks test case, temporarily replace the contents of `students.csv` with:

```csv
Name,Marks,Income,Attendance
Amit,abc,250000,80
```

Run the program and select option 1. It should print an invalid-marks message and skip Amit's row. Restore the original sample CSV after testing.
