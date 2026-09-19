# CDT Academy Submission

> **Cinazmo Data Technologies (CDT)**
>
> Azure AI Data Engineer Pathway

---

# Submission Information

| Field | Value |
|--------|-------|
| Module | Module 00 – Engineering Foundations |
| Lab | Lab 06 - Building Your First ETL Pipeline |
| Version | 1.0.0 |
| Date | 14 Sept 2026 |
| Student | Gavin McCraith-Smith |

---

# Objective

Importing data from a CSV file into SQL database using python.

---

# Environment Information

## Computer

| Item | Value |
|------|-------|
| Device | Apple Silicon M5 |
| Operating System | macOS Tahoe 26.6 |
| Terminal | zsh |

---

# Tasks Completed

| Task | Status |
|------|:------:|
| Engineering Journal Updated | y |
| Quick Reference Updated | y |

---

# Command Output

## Homebrew

```text
brew --version
```

Output

```text
Homebrew 6.0.14
```

---

## Docker

```text
docker --version
```

Output

```text
Docker version 29.6.2, build dfc4efb
```

---

## Azure CLI

```text
az version
```

Output

```text
  "azure-cli": "2.88.0",
  "azure-cli-core": "2.88.0",
  "azure-cli-telemetry": "1.1.0",
  "extensions": {}
```

---

## PowerShell

```text
pwsh --version
```

Output

```text
PowerShell 7.6.4
```

---

## VS Code CLI

```text
code --version
```

Output

```text
1.131.0
e4c7e7b1d6d060162f4aa7f8225271b67ce1df75
arm64
```

---

# Issues Encountered

Describe any issues encountered.

Include:

- Error messages
- Resolution
- Whether further investigation is required

If none:

> None encountered.

Met an issue where I was unable to run the import of the CSV files due to encoding issues. 

(.venv) gavinmccraith-smith@Gavins-MacBook-Air-2 python-sql-connection % python import-sales.py
Traceback (most recent call last):
  File "/Users/gavinmccraith-smith/Development/CDT-Academy/cdt-azure-ai-data-engineer-academy/projects/python-sql-connection/import-sales.py", line 29, in <module>
    row["StoreName"],
    ~~~^^^^^^^^^^^^^
KeyError: 'StoreName'

This was resolved by updating the Python script to include the encoding type to use for reading the CSV file(s). 

---

# Challenge Questions

## Question 1

Parameter placeholders allow for holding of temporary information that can then be recalled. If we were to use string concatenation, this may have to be repeated and may cause inconstancy.

---

## Question 2

CSV files cannot contain 2 million rows. They are limited to 1.024 or so million rows.

---

## Question 3

If there were 500 stores, we would need to update the Python program to allow for reading of multiple files instead of one file as this information would not be corrected into a single CSV file which the program is expecting currently. 

---

# Reflection

## What did I learn today?

How to import CSV files to a database using Python and how to troubleshoot encoding issues. 

---

## What challenged me?

As I haven't done any coursework for a month, I had to go through the process of setting up the environment before I could go through the course steps. i.e. starting docker, connecting to Python instance, etc. This hasn't been something I've had to do previously as during the first 5 modules I left everything open and running on the MacBook.

Troubleshooting the encoding issue was also a challenge. Searching online to try to resole the issue didn't yield the results to resolve the issue.

---

## What would I like to understand better?

The structure of the python scripts, though this will be covered in future Module so I look forward to being able to understand what these scripts do.

---

## What can I apply immediately?

As someone who uses MS SQL on a daily bases and deals with all multiple formats of data, i.e. CSV files, Access databases, Excel files, DBF files, etc. I can try to use Python to import these to SQL rather than running them through the UI. 

---

# Lessons Learned

Record technical lessons rather than personal reflections.

Example:

- Loading CSV files to SQL Databases via Python.
- Troubleshooting data formats prior to import. 

---

# Commands Learned

Record every new command introduced during this lab.

| Command | Purpose |
|----------|---------|
|  |  |
|  |  |

---

# Time Taken

Approximately: 1.5 hrs

---

# Self Assessment

| Area | Rating (1–5) |
|------|:------------:|
| Understanding | 4 |
| Confidence | 4 |
| Practical Ability | 3 |
| Documentation Quality | 5 |

---

# Ready to Progress?

☐ Yes


---

# Mentor Review (Completed by CDT)

| Category | Result |
|----------|--------|
| Technical Review | |
| Documentation | |
| Engineering Standards | |
| Understanding | |
| Overall Result | PASS / REVISIT |

Mentor Comments

(To be completed during review.)

---

# Version History

| Version | Date | Notes |
|----------|------|-------|
| 1.0.0 | DD Month YYYY | Initial Submission |
