# CDT Academy Submission

## Module
Module 00 - Engineering Foundations

## Lab
Lab 02 - Building Your Professional Azure Engineering Workstation

## Date
02 August 2026

---

# Command Output 

## brew --version

```text
Homebrew 6.0.14
```

## docker --version

```text
Docker version 29.6.2, build dfc4efb
```

## az version

```text
  "azure-cli": "2.88.0",
  "azure-cli-core": "2.88.0",
  "azure-cli-telemetry": "1.1.0",
  "extensions": {}
```

## pwsh --version

```text
PowerShell 7.6.4
```

## code --version

```text
1.131.0
e4c7e7b1d6d060162f4aa7f8225271b67ce1df75
arm64
```

---

# Installation Issues

Has a slight bit of issues installing PowerShell - there were a couple of things to be run in order to install this fully which i didn't notice in the terminal results, i only noticed the one so had to go back and double check the prompts 


# Mentor's Corrections

## Initial Understanding

CDT Challenge (Optional)
Can you answer these questions without searching online?
Why might Docker be preferable to installing SQL Server directly on your Mac? -- Docker would be preferable as SQL Server is a windows based product that does not work / install on Mac. To use this we would need to se up a virtual windows environment and would involve not being able to run queires directly on mac which is what we are trying to do whenever possible.
What advantages does Azure CLI offer over using only the Azure Portal? -- This should allow us to run and control everything directly on the Mac and use integrations easier where as the Azure portal i would assume does not have as much functionality.
Why would an engineer use PowerShell instead of Bash in a Microsoft-focused environment? PowerShell is a native Windows application and comes pre installed and usable as part of Windows. Using Bash within a MS focused environment would be adding additional and unnecessary steps

---

## Refined Understanding

Question 1
Why might Docker be preferable to installing SQL Server directly on your Mac?

Your Answer
Docker would be preferable as SQL Server is a windows based product that does not work / install on Mac. To use this we would need to set up a virtual windows environment...

Review
Score: 8.5/10
Good reasoning, but I'd refine one technical point.
SQL Server is no longer Windows-only. Microsoft provides SQL Server images for Linux, and Docker runs Linux containers on macOS. That's how we'll run SQL Server during the academy—without needing a Windows virtual machine.
So the bigger reason isn't "because SQL Server is Windows-only" but rather:
Docker gives us a clean, isolated environment.
We can start and stop SQL Server whenever we need it.
We don't clutter our Mac with a full database installation.
Every student (or engineer) gets an identical environment.
If something breaks, we can delete the container and recreate it in minutes.
In enterprise environments, Docker also makes it much easier to share development environments across teams.
CDT Mentor Tip: Containers are about consistency and portability, not just compatibility.

Question 2
What advantages does Azure CLI offer over using only the Azure Portal?

Your Answer
This should allow us to run and control everything directly on the Mac and use integrations easier...

Review
Score: 9/10
Excellent instinct.
You already recognised one of the biggest advantages:
Automation.
The Portal is excellent for:
exploring resources,
learning Azure,
occasional administration.
The Azure CLI is excellent for:
scripting,
automation,
repeatable deployments,
CI/CD,
infrastructure as code,
managing hundreds of resources consistently.
A good way to think about it is:
Azure Portal is for people. Azure CLI is for engineers.

That's an oversimplification, but it's a useful mental model.
Question 3
Why would an engineer use PowerShell instead of Bash in a Microsoft-focused environment?

Your Answer
PowerShell is a native Windows application...

Review
Score: 8/10
Good reasoning, but here's an important refinement.
PowerShell did begin as a Windows-only technology, but today PowerShell 7 is fully cross-platform, which is why you've just installed it on your Mac.
The bigger reasons Microsoft-focused organisations use PowerShell are:
It integrates deeply with Microsoft products (Azure, Microsoft 365, Windows Server, Active Directory, Exchange, etc.).
It works with objects, not just plain text.
Microsoft publishes a huge ecosystem of PowerShell modules.
Many enterprise automation scripts are written in PowerShell.
Bash is fantastic for Unix/Linux tooling, while PowerShell shines when you're automating Microsoft environments.
As an Azure engineer, you'll become comfortable using both, and one of our goals is to help you choose the right tool for the job.

---

## Key Takeaway

Learning about all the softwares we will use and why they are helpful.
