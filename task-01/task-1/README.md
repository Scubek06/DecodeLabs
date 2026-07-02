# Password Strength Checker

A beginner-friendly cybersecurity project that evaluates a password and classifies it as **Weak**, **Medium**, or **Strong**. The project demonstrates string handling, conditional logic, password security fundamentals, entropy estimation, testing, and secure coding habits.

## Requirement Analysis

The program must inspect a password and answer one simple question: how resistant is this password to guessing attacks?

Mandatory checks:

- **Length:** longer passwords create more possible combinations.
- **Uppercase letters:** increases variety and makes simple lowercase guesses less effective.
- **Lowercase letters:** supports normal alphabetic complexity.
- **Numbers:** adds another character class attackers must account for.
- **Special characters:** expands the search space beyond letters and digits.
- **Strength result:** gives the user a clear Weak, Medium, or Strong classification.

Security note: password validation does not make a system secure by itself. Real applications also need secure password hashing, rate limiting, multi-factor authentication, breached-password checks, and safe account recovery.

## Cybersecurity Concepts

### Password Entropy

Entropy estimates how unpredictable a password is. A password with more length and a larger character pool usually has more entropy. For example, `Summer2026!` looks mixed, but it still contains a predictable word and year pattern. Entropy formulas are useful for learning, but real attackers use smarter guessing strategies.

### Brute Force Attacks

A brute force attack tries many possible combinations until one works. Longer passwords make brute force much harder because every extra character multiplies the number of guesses.

### Dictionary Attacks

A dictionary attack tries known words, leaked passwords, names, seasons, years, and common patterns. This is why passwords like `Password123!` are still weak even though they contain multiple character types.

### Credential Stuffing

Credential stuffing uses usernames and passwords leaked from one service to break into another service. Users should never reuse passwords across accounts.

### Why Longer Passwords Are Stronger

Length usually matters more than symbol tricks. `correct-horse-battery-staple` style passphrases can be strong because they are long and memorable, while `P@ss1!` is short and easy to attack.

### Industry Password Policy Guidance

Modern policies commonly recommend:

- At least 12 characters for normal users.
- Longer passwords or passphrases for privileged accounts.
- Blocking common and breached passwords.
- Avoiding forced frequent password changes unless compromise is suspected.
- Encouraging password managers and multi-factor authentication.

## Project Architecture

```text
Cyber-Security P1/
├── password_strength_checker.py
├── tests/
│   └── test_password_strength_checker.py
└── README.md
```

Core components:

- `PasswordAnalysis`: structured result object for all analysis data.
- `analyze_password()`: main function that evaluates a password.
- `calculate_score()`: converts validation checks and entropy into a 0-100 score.
- `estimate_entropy_bits()`: educational entropy estimator.
- `build_recommendations()`: gives user-friendly improvement advice.
- `generate_password()`: creates a strong random password suggestion.
- `run_cli()`: command-line interface using hidden password input.

## Development Roadmap

1. Understand the password rules and why they matter.
2. Build small validation functions for uppercase, lowercase, numbers, symbols, and length.
3. Combine the checks into a score.
4. Convert the score into Weak, Medium, or Strong.
5. Add entropy estimation.
6. Add common weak password detection.
7. Add recommendations and password generation.
8. Add unit tests for normal, edge, and security cases.
9. Review the code for security and maintainability.
10. Improve the project with a GUI, breached-password API check, or password manager integration.

## How To Run

Use Python 3.10 or newer.

```bash
python password_strength_checker.py
```

On Windows, this may also work:

```bash
py password_strength_checker.py
```

## How To Test

```bash
python -m unittest discover -s tests
```

Or on Windows:

```bash
py -m unittest discover -s tests
```

## Sample Inputs And Outputs

| Password | Expected Result | Why |
| --- | --- | --- |
| `123456` | Weak | Very common and only numbers |
| `password1` | Weak | Common leaked-style password |
| `Aa1!` | Weak | Has variety but is too short |
| `Decode2026` | Medium | Decent length but no symbol |
| `D3c0deLabs!2026` | Strong | Long and uses multiple character classes |

## Test Plan

Normal test cases:

- Strong mixed password should be classified as Strong.
- Medium password should be classified as Medium.
- Short mixed password should still be Weak.

Edge cases:

- Empty password.
- Password with only numbers.
- Password with only letters.
- Very long password.
- `None` input should be rejected by the analyzer.

Security test cases:

- Common password must be Weak.
- Password generator must include uppercase, lowercase, digit, and symbol.
- Entropy should increase as length increases.
- Generated password length below 12 should be rejected.

## Code Review Notes

Current self-review rating: **8.5/10**

Strengths:

- Modular functions make the code easy to test.
- Password input is hidden in the CLI.
- Passwords are not logged or stored.
- Uses `secrets` instead of `random` for password generation.
- Includes unit tests for edge and security cases.

Improvements for a later version:

- Add Have I Been Pwned k-anonymity API support to detect breached passwords.
- Add zxcvbn-style pattern detection for names, dates, keyboard walks, and repeated sequences.
- Add a GUI or web interface.
- Add packaging metadata and continuous integration.

## Resume Project Description

Built a Python Password Strength Checker that classifies passwords as Weak, Medium, or Strong using length, character-class validation, common-password detection, score calculation, entropy estimation, and secure password generation. Added modular code, input validation, exception handling, and unit tests covering normal, edge, and security scenarios.

## LinkedIn Project Description

I completed a cybersecurity project: **Password Strength Checker**. The tool evaluates password strength using length, uppercase/lowercase letters, numbers, symbols, common weak password detection, entropy estimation, and a percentage strength meter. This project helped me practice secure coding, password security fundamentals, testing, and beginner-friendly security engineering design.

## Viva Interview Questions And Answers

**Q1. What is the objective of this project?**  
To evaluate a password and classify it as Weak, Medium, or Strong based on security rules.

**Q2. Why is password length important?**  
Each extra character increases the number of possible combinations an attacker may need to try.

**Q3. What is password entropy?**  
Entropy is an estimate of password unpredictability, usually measured in bits.

**Q4. Is `Password123!` strong?**  
No. It follows a common pattern and can appear in attacker dictionaries.

**Q5. What is a brute force attack?**  
An attack that tries many possible combinations until the correct password is found.

**Q6. What is a dictionary attack?**  
An attack that tries common words, leaked passwords, and predictable patterns.

**Q7. What is credential stuffing?**  
Using leaked credentials from one service to attempt login on another service.

**Q8. Why use `secrets` for password generation?**  
`secrets` is designed for cryptographic randomness, while `random` is predictable and not suitable for security-sensitive generation.

**Q9. Should applications store plain-text passwords?**  
No. They should store salted password hashes using algorithms like Argon2id, bcrypt, or scrypt.

**Q10. What future improvement would make this project more realistic?**  
Adding breached-password checks and advanced pattern detection would make the analysis closer to real-world password auditing.
