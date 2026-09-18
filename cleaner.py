import csv
import os
from datetime import datetime

INPUT_DIR = "input"
OUTPUT_DIR = "output"


def clean_string(value):
    """Trims whitespace and handles empty/null states."""
    if not value or value.strip().lower() in ["na", "n/a", "null", "none", ""]:
        return ""
    return value.strip()


def standardize_date(date_str):
    """Attempts to parse messy dates and normalize them to YYYY-MM-DD."""
    date_str = clean_string(date_str)
    if not date_str:
        return ""

    # Common date formats to test
    formats = ["%m/%d/%Y", "%m-%d-%Y", "%Y/%m/%d", "%Y-%m-%d", "%b %d, %Y"]
    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
    return date_str  # Return original if it doesn't match standard patterns


def process_csv(input_filename, output_filename):
    input_path = os.path.join(INPUT_DIR, input_filename)
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    if not os.path.exists(input_path):
        print(f"Error: Could not find file at {input_path}")
        return

    cleaned_rows = []

    with open(input_path, mode="r", encoding="utf-8-sig", errors="replace") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        if not fieldnames:
            print("Error: CSV file appears to be empty or missing headers.")
            return

        for row in reader:
            # Skip completely empty rows
            if not any(row.values()):
                continue

            # Clean each field in the row
            cleaned_row = {}
            for key, val in row.items():
                clean_key = clean_string(key)
                # Apply custom cleaning rules based on column names if needed
                if "date" in clean_key.lower():
                    cleaned_row[clean_key] = standardize_date(val)
                elif "name" in clean_key.lower() or "city" in clean_key.lower():
                    cleaned_row[clean_key] = clean_string(val).title()
                elif "email" in clean_key.lower():
                    cleaned_row[clean_key] = clean_string(val).lower()
                else:
                    cleaned_row[clean_key] = clean_string(val)

            cleaned_rows.append(cleaned_row)

    # Write cleaned data to output
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(output_path, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

    print(f"Success! Cleaned {len(cleaned_rows)} rows. Saved to {output_path}")


if __name__ == "__main__":
    print("--- 1-Click Data Sanitizer ---")
    # Example test run (ensure you drop a sample.csv into the input folder first)
    target_file = input("Enter the filename in the 'input' folder to clean (e.g., messy_data.csv): ").strip()
    if target_file:
        base_name, ext = os.path.splitext(target_file)
        output_file = f"{base_name}_cleaned{ext}"
        process_csv(target_file, output_file)