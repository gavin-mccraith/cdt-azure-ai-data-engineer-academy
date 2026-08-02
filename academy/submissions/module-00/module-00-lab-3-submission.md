# CDT Academy Submission

> **Cinazmo Data Technologies (CDT)**
>
> Azure AI Data Engineer Pathway

---

# Submission Information

| Field | Value |
|--------|-------|
| Module | Module 00 – Engineering Foundations |
| Lab | Lab 03 – Professional GitHub & Repository Foundation |
| Version | 1.0.0 |
| Date | 02 August 2026 |
| Student | Gavin McCraith-Smith |

---

# Objective

Set up GitHub repository and submit first comit via Git through terminal.

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
| Homebrew Installed | y |
| Docker Installed | y |
| Azure CLI Installed | y |
| PowerShell Installed | y |
| VS Code CLI Configured | y |
| Engineering Journal Updated | y |
| Quick Reference Updated | n |

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

- Error messages: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/gavin-mccraith/cdt-azure-ai-data-engineer-academy.git/'
- Resolution: password would not be accepted so generated an auth token from GitHub instead
- Whether further investigation is required: n/a


---

# Challenge Questions

## Question 1

We commit frequently so that version changes / updates can be tracked. This means should anything go wrong, we have restore points we can go back to.

---

## Question 2

an engineer shouldn't simply work on the main branch as updates and changes should be tested and reviewed prior to being released. This stops any potential bugs being released to a live environment and breaking / haulting use

---

## Question 3

Git keeps a record of all versions and changes where as something like a OneDrive backup will overwrite previou versions

---

# Reflection

## What did I learn today?

How to create a GitHub repository and push first commit via Git on the terminal.

---

## What challenged me?

learning how to log in to GitHub via terminal as the password was looking for a token instead

---

## What would I like to understand better?

How to look through the GitHub repository for previous version changes. Though i believe this will be covered as the course goes on.

---

## What can I apply immediately?

best practises for regular commits and not just "when things are done"

---

# Lessons Learned

Record technical lessons rather than personal reflections.

Example:

- How to create a GitHub repository.
- How to connect to GitHub via terminal.
- How to submit first commit.

---

# Commands Learned

Record every new command introduced during this lab.

| Command | Purpose |
|----------|---------|
| git status | check status of the repository |
| git add . | stage everything |
| git commit -m "" | send commit |
| git remote add origin <repository-url> | connect to repository |
| git branch -M main | connect to main branch of repo |
| git push -u origin main | send commit to main branch |

---

# Time Taken

Approximately: 70 mins

---

# Self Assessment

| Area | Rating (1–5) |
|------|:------------:|
| Understanding | 4 |
| Confidence | 4 |
| Practical Ability | 5 |
| Documentation Quality | 5 |

---

# Ready to Progress?

Yes

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
| 1.0.0 | 02 August 2026 | Initial Submission |
