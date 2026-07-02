# Cybersecurity Mini-Projects Portfolio

This repository contains a curated collection of Python-based security engineering tools designed to demonstrate defensive programming patterns, cryptographic principles, and automated test-driven development methodologies.

---

## 📂 Portfolio Architecture

```text
Cybersecurity-Portfolio/
├── P1_Password_Strength_Checker/
│   ├── password_strength_checker.py
│   └── tests/
│       └── test_password_strength_checker.py
├── P2_Basic_Encryption_Decryption/
│   ├── src/
│   │   └── encryption_tool/
│   │       ├── __init__.py
│   │       ├── caesar.py
│   │       ├── analysis.py
│   │       ├── file_crypto.py
│   │       └── cli.py
│   └── tests/
│       └── test_caesar.py
├── requirements.txt
├── LICENSE
└── README.md

🚀 Project Overviews
🛡️ Project 1: Password Strength Checker
An intelligent validation utility designed to audit credential security against automated guessing vectors.
Rather than relying solely on surface-level character checklists, the script estimates educational bit-entropy profiles to evaluate mathematical unpredictability.
It features dictionary isolation checks to identify common leaked combinations and utilizes the cryptographically secure secrets module to suggest structurally sound, strong fallback passphrases.

🔑 Project 2: Basic Encryption & Decryption Toolkit
An educational symmetric cryptography sandbox centered on the mechanics of classical substitution ciphers.
The package includes multi-pass text and local file-stream encryption engines utilizing a user-defined shift key.
To demonstrate practical cryptanalysis, the tool also implements automated brute-force decryption modules alongside alphabetic character frequency trackers to illustrate why legacy algorithms fail modern compliance requirements.
