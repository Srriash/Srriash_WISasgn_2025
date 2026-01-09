# Submissions Report (Yes/No)

This folder contains a script that reads `subjects.txt` and generates a submission
status report for Days 01-09.

## What it does

- Creates a table showing whether each student submitted each assignment.
- Exports the table to an Excel file `submission_report.xlsx` (or a timestamped
  filename if the file is locked).

## Logic used

- Each line in `subjects.txt` is split by tabs and the subject is parsed.
- The day is detected with a regex matching `Day` and a number (e.g., `Day08`).
- The student name is detected from `by <name>` or from a trailing `- <name>`.
- Names are normalized to reduce duplicates:
  - Case-insensitive comparison (e.g., `Rachel` vs `rachel`).
  - Removes punctuation/quotes and extra spaces.
  - Splits camel case (e.g., `SteinitzEliyahu` -> `Steinitz Eliyahu`).
- A student is marked as `yes` for a day if any matching issue exists.
- Day 07 has no assignment and is shown as `-`.

## How to run

```
python report.py
```

## Files

- `report.py`: The report generator.
- `subjects.txt`: Input data.
- `submission_report.xlsx`: Output (generated).

## AI prompt used (codex chatgpt 5.2)

"Given the data in the day09/subjects.txt file in this repo
write a program that will create a report of Missing submissions per assignment: list students with no “DayXX” issue by deadline. Create a python program as report.py
using the subjects.txt file on the day_09 folder of this repo. Create a table
with all the students name on the first column then following rows starting with
day 1 till day 9. For day 7 just put a dash. Export to Excel. Account for
capitalization differences and name formatting."
