# CYB_333_Shaw_Project
CYB 333 Course Project Code File
# Password Strength Analyzer 🛡️

A clean, lightweight security automation utility written in Python to programmatically evaluate credential resilience against brute-force guessing and dictionary attack configurations.

---

## 🎯 Project Objectives

Traditional access controls forced strict "composition complexity constraints" (e.g., demanding a capital letter and symbol in exact spots), leading users to generate predictable combinations like `Password123!`. 

This project follows modern **NIST SP 800-63B guidelines** by shifting focus toward:
1. **Absolute Length Optimization:** Incentivizing long passphrases that offer higher mathematical entropy.
2. **Predictable String Rejection:** Programmatically identifying and filtering out common dictionary sequences and keyboard walks.
3. **Actionable Remediation:** Supplying instant, readable improvement lists to users during input.

---

## ✨ Features and Logic Matrix

* **Multi-Tiered Length Verifier:** Awards points dynamically depending on overall string size ($<8$ characters, $8-11$ characters, or optimal $\ge12$ characters).
* **Native Character Set Parser:** Inspects text using standard, highly legible boolean methods (`islower()`, `isupper()`, `isdigit()`, `isalnum()`) to confirm structural diversity.
* **Malicious Sequence Blocker:** Runs case-insensitive checks against a blacklisted pattern dictionary (`qwerty`, `12345`, etc.) and penalizes the metrics score by 2 points if matches are uncovered.
* **Granular Suggestion Array:** Compiles and prints targeted refinement actions dynamically based on exactly what elements the password is missing.

---

## 📋 Dependencies and Prerequisites

* **Python Version:** Python 3.8 or higher is required.
* **Libraries:** This script relies exclusively on native Python logic structures. **No external dependencies or third-party packages (such as `pip` installations) are required.** This keeps the utility lightweight, fast, and completely safe to run in isolated laboratory spaces.

---

## ⚙️ Setup and Installation Instructions

Follow these steps to run the application within the **PyCharm IDE**:

### Step 1: Create a Sandbox Project Space
1. Launch **PyCharm**.
2. Select **New Project** from the greeting dashboard (or navigate to **File > New Project** via the top directory).
3. Specify your project path location and ensure a clean **Virtualenv** environment structure is toggled. Click **Create**.

### Step 2: Establish the Script File
1. Locate the left-hand **Project tool pane**. Right-click your root project folder.
2. Select **New > Python File**.
3. Label the text file `analyzer` and hit `Enter` (PyCharm automatically creates `analyzer.py`).
4. Paste the documented code blocks into the empty script window.

---

## 🚀 Running the Script & Documenting Results

Because the security analyzer handles interactive live inputs, it executes within the terminal panel at the bottom of the IDE layout:

1. Right-click directly inside your code window workspace and click **Run 'analyzer'** (or use the `Shift + F10` shortcut).
2. Look at the **Run tool window** at the bottom of PyCharm to locate the active tracking prompt:
   ```text
   --- Password Strength Analyzer ---
   Enter a password to test:
