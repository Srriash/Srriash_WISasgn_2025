import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SUBJECTS_PATH = BASE_DIR / "subjects.txt"
REPORT_XLSX_PATH = BASE_DIR / "submission_report.xlsx"

DAY_RE = re.compile(r"\bday\s*0?(\d+)\b", re.IGNORECASE)
BY_RE = re.compile(r"\bby\b\s*(.+)$", re.IGNORECASE)


def normalize_name(raw: str):
    if not raw:
        return None, None
    expanded = re.sub(r"([a-z])([A-Z])", r"\1 \2", raw)
    expanded = expanded.replace('"', " ").replace("'", " ")
    cleaned = re.sub(r"[^A-Za-z]+", " ", expanded)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    key = cleaned.casefold()
    display = " ".join(part.capitalize() for part in cleaned.split(" "))
    return key, display


def parse_subject(subject: str):
    match = DAY_RE.search(subject)
    if not match:
        return None, None
    day_num = int(match.group(1))
    day_key = f"Day{day_num:02d}"

    by_match = BY_RE.search(subject)
    if by_match:
        name = by_match.group(1).strip(" -")
    else:
        hyphen_match = re.search(r"[-–—]\s*([A-Za-z].+)$", subject)
        if hyphen_match:
            name = hyphen_match.group(1).strip()
        else:
            cleaned = DAY_RE.sub("", subject)
            cleaned = re.sub(r"[-:]", " ", cleaned)
            cleaned = re.sub(r"\s+", " ", cleaned).strip()
            name = cleaned

    if not name:
        return day_key, None
    return day_key, name


def parse_issues(path: Path):
    roster = set()
    submissions = defaultdict(list)
    name_display = {}

    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 5:
                continue
            subject = parts[2].strip()
            created_str = parts[4].strip()
            try:
                created_at = datetime.fromisoformat(created_str.replace("Z", "+00:00"))
            except ValueError:
                continue

            day_key, name = parse_subject(subject)
            if name:
                key, display = normalize_name(name)
                if key:
                    roster.add(key)
                    name_display.setdefault(key, display)
            if day_key and name:
                key, display = normalize_name(name)
                if key:
                    submissions[(day_key, key)].append(created_at)

    return roster, submissions, name_display


def build_day_keys():
    return [f"Day{day_num:02d}" for day_num in range(1, 10)]


def format_table(title, header, rows):
    widths = [len(col) for col in header]
    for row in rows:
        for idx, cell in enumerate(row):
            widths[idx] = max(widths[idx], len(cell))

    def format_row(values):
        return " | ".join(value.ljust(widths[idx]) for idx, value in enumerate(values))

    line = "-+-".join("-" * width for width in widths)
    print(title)
    print(format_row(header))
    print(line)
    for row in rows:
        print(format_row(row))
    print()

def write_excel(path, header, submission_rows):
    try:
        from openpyxl import Workbook
    except Exception as exc:
        print(f"Excel export skipped (missing openpyxl): {exc}")
        return

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Submission Status"
    sheet.append(header)
    for row in submission_rows:
        sheet.append(row)

    try:
        workbook.save(path)
    except PermissionError:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        alt_path = path.with_name(f"{path.stem}_{timestamp}{path.suffix}")
        workbook.save(alt_path)
        print(f"Excel file locked, wrote {alt_path.name} instead.")


def main():
    if not SUBJECTS_PATH.exists():
        raise SystemExit(f"Missing {SUBJECTS_PATH}")

    roster, submissions, name_display = parse_issues(SUBJECTS_PATH)

    print("Report based on subjects.txt and deadlines.txt")
    print()

    day_keys = build_day_keys()
    ordered_names = sorted(roster, key=lambda key: name_display.get(key, key))

    submission_rows = []
    for name_key in ordered_names:
        display_name = name_display.get(name_key, name_key)
        submitted_row = [display_name]
        for day_key in day_keys:
            if day_key == "Day07":
                submitted_row.append("-")
                continue

            submitted_times = submissions.get((day_key, name_key), [])
            if submitted_times:
                submitted_row.append("yes")
            else:
                submitted_row.append("no")

        submission_rows.append(submitted_row)

    header = ["Student"] + day_keys
    format_table("Submission status (yes/no)", header, submission_rows)
    write_excel(REPORT_XLSX_PATH, header, submission_rows)
    print()
    print(f"Wrote {REPORT_XLSX_PATH.name}")


if __name__ == "__main__":
    main()
