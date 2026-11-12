# LogLens v1.0: Verified Facts (Do Not Edit)

**Purpose:** This is the authoritative fact sheet for the Assignment 3 editing exercise. The README and installation guide are intentionally flawed. If they conflict with this sheet or the included program, correct the documentation. Do not modify the program or this sheet.

## Intended readers

The primary audience is undergraduate computing students and new technical interns who understand basic CSV files and have used a terminal, but have not used LogLens. Do not assume that they know this repository's structure, commands, or flags.

## What the program does

- LogLens is a local, command-line Python script for counting records in a CSV log file.
- It reads but does **not** repair, rewrite, or otherwise modify the input CSV.
- It does **not** transmit, upload, or store the input data outside the user's computer.
- It does **not** diagnose system failures; it counts records by log level.
- It requires Python **3.10 or newer** and only uses the Python standard library. No `pip install` or third-party dependencies are needed.
- It expects CSV column headers named exactly `timestamp`, `level`, and `message`.
- Accepted log levels are `INFO`, `WARN`, and `ERROR` (uppercase). The `--level` argument is optional. When omitted, it counts all records.
- The `--file` argument is required. Run commands from the repository root, where `loglens.py` is located. Commands in examples use `python`; on some computers, the Python launcher is `python3` or `py` instead.

## Verified commands and output

From the repository root:

```bash
python loglens.py --file data/sample_logs.csv --level ERROR
```

Expected result:

```text
Records matching ERROR: 2
```

Or omit the optional level:

```bash
python loglens.py --file data/sample_logs.csv
```

Expected result:

```text
Records matching ALL: 6
```

To see valid command-line options:

```bash
python loglens.py --help
```

## Important constraints

- Both files should describe **the same** product and use consistent names and terminology.
- Write accurate instructions for obtaining the files from the repository, finding the repository root, and running the command.
- If discussing error reports or support, advise users not to post private or sensitive log data publicly. Prefer a description of the problem and a sanitized, minimal example.
- Do not invent features, flags, installation packages, websites, warranties, or platform-specific procedures that are not verified here.
