# 🧹 1-Click Python CSV & Data Sanitizer

A lightweight, zero-dependency Python utility designed to instantly clean, standardize, and format messy CSV datasets. Stop wasting hours manually fixing casing errors, weird date formats, and misaligned columns in spreadsheets.

---

## ✨ What It Fixes Automatically
* **Name & Location Formatting:** Automatically converts sloppy capitalization (e.g., `john DOE`, `new york`) into clean Title Case (`John Doe`, `New York`).
* **Email Normalization:** Forces all email addresses to lowercase to prevent duplicates and database errors.
* **Date Standardization:** Parses messy, inconsistent date formats (like `12/15/2024` or `03-22-2024`) and normalizes them into standard ISO format (`YYYY-MM-DD`).
* **Null & Empty Handling:** Cleans up broken text states like `n/a`, `NULL`, or whitespace-padded blank cells.
* **Safe Output Generation:** Leaves your raw data untouched and saves a clean, production-ready copy with a `_cleaned` suffix.

---

## 📂 Project Structure
```text
data_sanitizer/
│
├── input/
│   └── messy_data.csv        # <-- Drop your raw, unformatted CSVs here
├── output/
│   └── messy_data_cleaned.csv # <-- Cleaned, polished files appear here automatically
├── cleaner.py                 # <-- The core automation script
└── README.md                  # <-- Documentation & instructions