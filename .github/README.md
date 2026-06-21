# 🚀 Git_Automater

A Python-based Git automation tool that automatically updates a file, creates Git commits, and pushes changes to GitHub.

This project demonstrates automation using Python, Git commands, and Windows Task Scheduler.

---

## ✨ Features

* ✅ Automatically updates activity file
* ✅ Creates Git commits automatically
* ✅ Pushes changes to GitHub
* ✅ Runs in background
* ✅ No manual Git commands required
* ✅ Uses Python automation + Git workflow

---

## 🔥 Workflow

```
Laptop Login
      |
      ↓
Windows Task Scheduler
      |
      ↓
auto_commit.py runs
      |
      ↓
activity.txt updated
      |
      ↓
git add .
      |
      ↓
git commit
      |
      ↓
git push
      |
      ↓
GitHub Updated
```

---

## 📂 Project Structure

```
Git_Automater
│
├── auto_commit.py       # Main automation script
├── activity.txt         # Automatically updated file
├── .gitignore
├── README.md
└── venv                 # Python virtual environment
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/ReetRatri/Git_Automater.git
```

Go inside project:

```bash
cd Git_Automater
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows PowerShell

```powershell
.\venv\Scripts\activate
```

---

## 3. Run Manually

Start automation:

```bash
python auto_commit.py
```

The script will:

1. Update `activity.txt`
2. Add changes
3. Create a commit
4. Push changes to GitHub

---

# 🤖 Background Automation

This project uses Windows Task Scheduler.

Setup:

```
Trigger:
    When I log on

Action:
    Run auto_commit.py
```

After setup:

```
Start Laptop
      ↓
Task Scheduler
      ↓
Python Script
      ↓
Git Commit
      ↓
Git Push
```

---

# 🛠️ Requirements

* Python 3.x
* Git
* GitHub account

Check:

```bash
python --version
```

```bash
git --version
```

---

# 🧠 Concepts Used

* Python subprocess module
* File handling
* Git CLI automation
* Virtual environments
* Task scheduling
* Automation workflows

---

# 🚧 Future Improvements

* Custom commit messages
* Multiple repository support
* GUI dashboard
* Logging system
* Cross-platform support
* GitHub API integration

---

# 👨‍💻 Author

**Reet Choudhary**

Python Developer | Automation | Web Development

GitHub:
https://github.com/ReetRatri

---

⭐ Built for learning automation and improving development workflows.
