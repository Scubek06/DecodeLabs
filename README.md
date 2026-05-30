# Basic Encryption & Decryption

Project 2 in a cybersecurity learning portfolio. This project teaches encryption and decryption fundamentals using classical ciphers, starting with Caesar Cipher and expanding into analysis features.

## Requirement Analysis

Encryption converts readable plaintext into unreadable ciphertext using an algorithm and key. Decryption reverses that process when the correct key and algorithm are known.

This project uses Caesar Cipher for education. Caesar Cipher is not secure for real-world protection because an attacker can brute-force all possible shifts quickly, but it is excellent for learning substitution, keys, encryption flow, and cryptanalysis basics.

## Roadmap

1. Create professional project structure.
2. Implement Caesar Cipher encryption.
3. Implement Caesar Cipher decryption.
4. Add a menu-driven command-line interface.
5. Add brute-force decoding and frequency analysis.
6. Add encryption statistics.
7. Add file encryption support for text files.
8. Add tests for normal, edge, invalid, and security-focused cases.
9. Add complete documentation, resume content, LinkedIn content, and viva Q&A.

## Architecture

```text
Basic-Encryption-Decryption/
├── src/
│   └── encryption_tool/
│       ├── __init__.py
│       ├── caesar.py
│       ├── analysis.py
│       ├── file_crypto.py
│       └── cli.py
├── tests/
│   └── test_caesar.py
├── docs/
│   ├── architecture.md
│   └── internship_report.md
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## Security Warning

This project is for learning cryptography concepts. Caesar Cipher and Vigenere Cipher are not secure for protecting real data. Real systems should use vetted cryptographic libraries and modern algorithms such as AES-GCM, ChaCha20-Poly1305, RSA-OAEP, or elliptic-curve cryptography depending on the use case.

## Quick Start

```bash
python -m encryption_tool.cli
```

## Run Tests

```bash
python -m unittest discover -s tests
```
