# CDT Academy Submission

> **Cinazmo Data Technologies (CDT)**
>
> Azure AI Data Engineer Pathway

---

# Submission Information

| Field | Value |
|--------|-------|
| Module | Module 00 – Engineering Foundations |
| Lab | Lab 07 - Professional Configuration & Logging |
| Version | 2.1 |
| Date | 15 Sept 2026 |
| Student | Gavin McCraith-Smith |

---

# Objective

Set up a professional example of configuration of an ETL application in a consumer based enviroment, ensuring correct archiving of processed files and logging of issues is followed.

---

# Environment Information

## Computer

| Item | Value |
|------|-------|
| Device | Apple Silicon M5 |
| Operating System | macOS Golden Gate 27.0 |
| Terminal | zsh |

---

# Tasks Completed

| Task | Status |
|------|:------:|
| python-dotenv | y |
 |
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

> Issue updating the python script due to some ambiguity in the reference. This was resolved by updating the details of the course.

---

# Challenge Questions

## Question 1

.env files should never be commited to git as they will contain sensitive information like passwords, server names, etc. 

---

## Question 2

Log files are useful as it stores a record of what has been processed, if something has been successful and prints errors. these can be used by an engineer to try to figure out what cause an issue or where an event happened. 

---

## Question 3

A loop should be created in the code that looks at the folder incoming/ processes a file then moves it to archived/ - this process should loop until there are no longer any files in the incoming/ folder left to process.

---

# Reflection

## What did I learn today?
Learned setting up configuration files, error and exception logging.
---

## What challenged me?
some of the code updates that weren't clear exactly where they should be placed.
---

## What would I like to understand better?
Code structure and placement. However as previously with the previoud Lab, this wil be covered when we move on the the Pyhon section(s).
---

## What can I apply immediately?
Creating configuration and logging files for any other projects or work i'm working on in my day to day job
---

# Lessons Learned

Record technical lessons rather than personal reflections.

Example:

- Configuration files can be created and used to store sensitive information you do not want to release with code files. 
- Creating log files is an essential part of developement.

---

# Commands Learned

Record every new command introduced during this lab.

| Command | Purpose |
|----------|---------|
|  pip install python-dotenv | used to load environmental variables |

---

# Time Taken

Approximately: 2 hours

---

# Self Assessment

| Area | Rating (1–5) |
|------|:------------:|
| Understanding | 4 |
| Confidence | 4 |
| Practical Ability | 4 |
| Documentation Quality | 4 |

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
