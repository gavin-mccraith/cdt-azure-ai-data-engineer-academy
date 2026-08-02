# CDT Academy Submission

> **Cinazmo Data Technologies (CDT)**
>
> Azure AI Data Engineer Pathway

---

# Submission Information

| Field | Value |
|--------|-------|
| Module | Module 00 – Engineering Foundations |
| Lab | Lab 04 - Containerisation with Docker |
| Version | 1.0.0 |
| Date | 02 August 2026 |
| Student | Gavin McCraith-Smith |

---

# Objective

Learn what Docker is and how to use it - creating first SQL instance and running it and connecting to the server via VS Code. 

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

No issues encountered.

---

# Challenge Questions

## Question 1

Deleting the container only removes the locally created instance, not the whole image. Some of this data may not be contained in the container but within the image blueprint itself.

---

## Question 2

Docker would make this easier at it would allow all ten developers to run the same version / instance / setup of an application. This saves any potential conflict if difference developers are running difference versions of software.

---

## Question 3

Containers may be advantageous over virtual machines due to their consistancy across multiple users / machines where as VMs may become outdated on versions. 
Additionally, VM connections can drop / go offline where as a local docker instance wouldn't.

---

# Reflection

## What did I learn today?

Leanred how to download images and create containers for SQL2022 and connect to it vis VS Code.

---

## What challenged me?

I didn't find anything particular challenging dueing this Lab, however understanding the docker prompts will take some time to become firm in memory.

---

## What would I like to understand better?

Nothing at this moment, but look forward to learning / using more of docker and what it can do and how it can be applied as the course progresses.

---

## What can I apply immediately?

The use of SQL insrances created from Docker.

---

# Lessons Learned

Record technical lessons rather than personal reflections.

Example:

- Docker containers provide isolated development environments.
- SQL instances can be created via docker with much ease compared to a local install of a server on a Windows machine. 
- multiple containers can be made from a single image as the image is the blueprint from which a container can be created.

---

# Commands Learned

Record every new command introduced during this lab.

| Command | Purpose |
|----------|---------|
| docker images | view what images are available for use |
| docker ps | view which containers are running |

---

# Time Taken

Approximately: 120 mins

---

# Self Assessment

| Area | Rating (1–5) |
|------|:------------:|
| Understanding | 4 |
| Confidence | 4 |
| Practical Ability | 4 |
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
