"""
Project No. 62: Student Scholarship Eligibility Analyzer
Language: Python 3
Library: Pandas

Run from the terminal:
    python main.py

The program reads students.csv from the same folder.
"""

from pathlib import Path
import pandas as pd

CSV_FILE = Path(__file__).with_name("students.csv")

# Scholarship rules from the project description
MIN_MARKS = 75
MIN_ATTENDANCE = 75
MAX_INCOME = 500000
FULL_MARKS = 90
FULL_INCOME_LIMIT = 300000
FULL_AMOUNT = 50000
PARTIAL_AMOUNT = 25000

REQUIRED_COLUMNS = ["Name", "Marks", "Income", "Attendance"]


def load_students(file_path):
    """Load the CSV file and skip rows that contain invalid or missing data."""
    try:
        data = pd.read_csv(file_path, dtype={"Name": "string"})
    except FileNotFoundError:
        print(f"Error: Could not find '{file_path.name}'. Keep it in the same folder as main.py.")
        return pd.DataFrame(columns=REQUIRED_COLUMNS)
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        return pd.DataFrame(columns=REQUIRED_COLUMNS)
    except Exception as error:
        print(f"Error while reading the CSV file: {error}")
        return pd.DataFrame(columns=REQUIRED_COLUMNS)

    # Check that the CSV has all required headings.
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in data.columns]
    if missing_columns:
        print("Error: Missing CSV column(s): " + ", ".join(missing_columns))
        return pd.DataFrame(columns=REQUIRED_COLUMNS)

    valid_rows = []

    for index, row in data.iterrows():
        row_number = index + 2  # Header is on line 1.
        name = row["Name"]

        if pd.isna(name) or not str(name).strip():
            print(f"Invalid or missing name at CSV row {row_number}. Row skipped.")
            continue

        converted = {}
        row_is_valid = True

        for column in ["Marks", "Income", "Attendance"]:
            value = pd.to_numeric(row[column], errors="coerce")

            if pd.isna(value):
                print(f"Invalid or missing {column.lower()} for {str(name).strip()}: '{row[column]}'. Row skipped.")
                row_is_valid = False
                break

            converted[column] = float(value)

        if not row_is_valid:
            continue

        # Values outside their normal ranges are treated as invalid input.
        if not 0 <= converted["Marks"] <= 100:
            print(f"Invalid marks for {str(name).strip()}: '{row['Marks']}'. Row skipped.")
            continue

        if not 0 <= converted["Attendance"] <= 100:
            print(f"Invalid attendance for {str(name).strip()}: '{row['Attendance']}'. Row skipped.")
            continue

        if converted["Income"] < 0:
            print(f"Invalid income for {str(name).strip()}: '{row['Income']}'. Row skipped.")
            continue

        valid_rows.append({
            "Name": str(name).strip(),
            "Marks": converted["Marks"],
            "Income": converted["Income"],
            "Attendance": converted["Attendance"]
        })

    return pd.DataFrame(valid_rows, columns=REQUIRED_COLUMNS)


def decide_scholarship(row):
    """Return eligibility status, scholarship category and amount for one student."""
    eligible = (
        row["Attendance"] >= MIN_ATTENDANCE
        and row["Marks"] >= MIN_MARKS
        and row["Income"] <= MAX_INCOME
    )

    if not eligible:
        return pd.Series(["Not Eligible", 0])

    if row["Marks"] >= FULL_MARKS and row["Income"] <= FULL_INCOME_LIMIT:
        return pd.Series(["Full", FULL_AMOUNT])

    return pd.Series(["Partial", PARTIAL_AMOUNT])


def prepare_results(students):
    """Apply the scholarship conditions to every valid student."""
    if students.empty:
        result = students.copy()
        result["Scholarship"] = pd.Series(dtype="object")
        result["Amount"] = pd.Series(dtype="int64")
        return result

    result = students.copy()
    result[["Scholarship", "Amount"]] = result.apply(decide_scholarship, axis=1)
    result["Amount"] = result["Amount"].astype(int)
    return result


def show_eligibility(results):
    """Menu option 1: display each student's scholarship result."""
    if results.empty:
        print("\nNo valid student records are available.")
        return

    print("\nSTUDENT SCHOLARSHIP RESULTS")
    print("-" * 48)

    for _, student in results.iterrows():
        if student["Scholarship"] == "Not Eligible":
            print(f"{student['Name']} | Not Eligible")
        else:
            print(
                f"{student['Name']} | {student['Scholarship']} | "
                f"Rs. {int(student['Amount'])}"
            )


def show_summary(results):
    """Menu option 2: show counts, total amount and average eligible marks."""
    if results.empty:
        print("\nNo valid student records are available.")
        return

    eligible = results[results["Scholarship"] != "Not Eligible"]
    not_eligible_count = int((results["Scholarship"] == "Not Eligible").sum())
    full_count = int((results["Scholarship"] == "Full").sum())
    partial_count = int((results["Scholarship"] == "Partial").sum())
    total_amount = int(results["Amount"].sum())

    if eligible.empty:
        average_marks = 0.0
    else:
        average_marks = eligible["Marks"].mean()

    print("\nSCHOLARSHIP SUMMARY")
    print("-" * 48)
    print(f"Eligible: {len(eligible)} | Not Eligible: {not_eligible_count} | "
          f"Full: {full_count} | Partial: {partial_count}")
    print(f"Total scholarship: Rs. {total_amount} | "
          f"Average marks (eligible): {average_marks:.2f}")


def filter_by_marks(students):
    """Menu option 3: display all valid students at or above a chosen mark."""
    if students.empty:
        print("\nNo valid student records are available.")
        return

    try:
        minimum_marks = float(input("Enter minimum marks: ").strip())
    except ValueError:
        print("Please enter a valid number for minimum marks.")
        return

    if not 0 <= minimum_marks <= 100:
        print("Minimum marks must be between 0 and 100.")
        return

    selected = students[students["Marks"] >= minimum_marks].sort_values(
        by="Marks", ascending=False
    )

    print(f"\nSTUDENTS WITH MARKS >= {minimum_marks:g}")
    print("-" * 48)

    if selected.empty:
        print("No students found above the given marks.")
        return

    for _, student in selected.iterrows():
        marks = int(student["Marks"]) if student["Marks"].is_integer() else student["Marks"]
        print(f"{student['Name']} | {marks:g}")


def main():
    """Display the menu and run the selected operation."""
    students = load_students(CSV_FILE)
    results = prepare_results(students)

    while True:
        print("\n===== STUDENT SCHOLARSHIP ELIGIBILITY ANALYZER =====")
        print("1. Check scholarship eligibility")
        print("2. Show scholarship summary")
        print("3. Filter students by minimum marks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            show_eligibility(results)
        elif choice == "2":
            show_summary(results)
        elif choice == "3":
            filter_by_marks(students)
        elif choice == "4":
            print("Thank you for using the Scholarship Eligibility Analyzer.")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 4.")


if __name__ == "__main__":
    main()
