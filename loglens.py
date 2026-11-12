"""LogLens: count CSV log records by level. Included to verify the documentation."""

import argparse
import csv
from pathlib import Path

REQUIRED_COLUMNS = {"timestamp", "level", "message"}
LEVELS = ("INFO", "WARN", "ERROR")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Count records by level in a CSV log file (without modifying it)."
    )
    parser.add_argument("--file", required=True, help="Path to a CSV log file")
    parser.add_argument(
        "--level", choices=LEVELS, help="Optional level: INFO, WARN, or ERROR"
    )
    args = parser.parse_args()

    try:
        with Path(args.file).open("r", newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
                parser.error("CSV must contain timestamp, level, and message columns")
            count = sum(1 for row in reader if args.level is None or row["level"] == args.level)
    except FileNotFoundError:
        parser.error(f"File not found: {args.file}")
    except PermissionError:
        parser.error(f"Cannot read file: {args.file}")

    print(f"Records matching {args.level or 'ALL'}: {count}")


if __name__ == "__main__":
    main()
