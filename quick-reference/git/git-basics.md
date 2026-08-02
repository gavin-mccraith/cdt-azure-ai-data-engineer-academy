# Git Basics Quick Reference

## Inspect the repository

```bash
git status
```

Shows changed, staged, deleted, and untracked files.

```bash
git log --oneline
```

Shows a compact commit history.

## Stage changes

```bash
git add <file>
```

Stages one file.

```bash
git add .
```

Stages changes beneath the current directory.

## Commit changes

```bash
git commit -m "Describe the logical change"
```

## Work with a remote repository

```bash
git remote -v
```

Shows configured remotes.

```bash
git push
```

Pushes committed changes.

```bash
git pull
```

Retrieves and integrates remote changes.

## Restore an unstaged file

```bash
git restore <file>
```

Restores the working copy from the latest committed version.
