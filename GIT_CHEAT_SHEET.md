# Git Operations Cheat Sheet

This project uses Git for version control. Here are the core commands to manage your changes:

## 1. Stage Changes
Prepare your files for the next commit:
```bash
git add .
```

## 2. Commit
Save your changes locally:
```bash
git commit -m "Describe what you changed here"
```

## 3. Link or Update GitHub URL

**Link a new repository:**
```bash
git remote add origin https://github.com/ManuData/koda-stack.git
```

**Sync/Update existing URL (if wrong):**
```bash
git remote set-url origin https://github.com/ManuData/koda-stack.git
```

## 4. Push
Send your local commits to GitHub:
```bash
git push
```
*Note: We've already set up tracking, so `git push` is all you need for the `main` branch.*

---

### Troubleshooting common issues

#### Large Push Errors (HTTP 400)
If you see an error about push size, it's likely fixed by:
```bash
git config http.postBuffer 524288000
```
*(This has already been applied locally!)*

#### Check Status
To see which files are changed or what's ready to commit:
```bash
git status
```
