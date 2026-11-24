# Password Strength Analyzer

A beginner-friendly Python cybersecurity project that checks password strength, highlights missing security requirements, and suggests ways to improve a password. Includes a command-line interface and an interactive [Streamlit](https://streamlit.io/) web app.

Built for **BYU CS 111** as a personal programming project.

## Features

- Estimates password strength on a **0–100** scale, with Weak, Moderate, and Strong ratings
- Checks length, uppercase and lowercase letters, numbers, and supported special characters
- Flags matches from a small built-in list of common passwords
- Shows a security checklist and improvement suggestions in Streamlit
- Offers a simple command-line version

> **Security note:** This is an educational rules-based estimator, not a comprehensive password-security assessment. It checks only a small local list of common passwords; a high score does **not** guarantee that a password is secure. **Only enter made-up or test passwords**, especially on a publicly hosted demo. The application does not intentionally store passwords, but passwords entered in a hosted app are processed by its server.

## Run the Streamlit app

Requires Python 3.9 or newer.

1. Clone the repository and enter the project directory:

   ```bash
   git clone https://github.com/cyberseafoam/password-strength-analyzer.git
   cd password-strength-analyzer
   ```

2. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Start the application:

   ```bash
   python -m streamlit run app.py
   ```

Streamlit will display a local URL to open in your browser.

## Run the command-line version

The analyzer itself uses only standard Python:

```bash
python password_analyzer.py
```

Choose **1** to analyze a sample password or **2** to exit.

## Project structure

```text
password-strength-analyzer/
├── app.py                 # Streamlit web interface
├── password_analyzer.py   # Password checks, scoring, suggestions, CLI
├── requirements.txt       # Dependencies
├── .gitignore             # Excludes local/generated files
└── README.md              # Documentation
```

## How scoring works

The program adds points for meeting these checks:

| Check | Points |
| --- | ---: |
| At least 8 characters | 20 |
| At least 12 characters | 20 |
| At least 16 characters | 20 |
| Contains an uppercase letter | 10 |
| Contains a lowercase letter | 10 |
| Contains a number | 10 |
| Contains a supported special character | 10 |

Passwords matching the built-in common-password list get a score of **0**. Scores below 40 are **Weak**, 40–79 are **Moderate**, and 80–100 are **Strong**.

This score is a learning aid, not a measure of cracking resistance or a substitute for a password manager.

## Technologies

- Python
- Streamlit

## Possible future improvements

- Larger breached-password screening with privacy-preserving lookup
- More realistic strength estimation that accounts for predictable patterns
- Automated tests and a CI workflow
- A secure password generator using Python's `secrets` module

## About

Created as a CS 111 free coding project at Brigham Young University to practice Python programming and explore cybersecurity concepts.
