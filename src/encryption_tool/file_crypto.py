"""Text-file helpers for educational encryption workflows."""

from __future__ import annotations

from pathlib import Path

from encryption_tool.caesar import decrypt, encrypt


def read_text_file(file_path: str) -> str:
    """Read a UTF-8 text file."""

    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    return path.read_text(encoding="utf-8")


def write_text_file(file_path: str, content: str) -> None:
    """Write UTF-8 text to a file."""

    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def encrypt_file(input_path: str, output_path: str, shift: int) -> None:
    """Encrypt a text file and write the result to another file."""

    plaintext = read_text_file(input_path)
    ciphertext = encrypt(plaintext, shift)
    write_text_file(output_path, ciphertext)


def decrypt_file(input_path: str, output_path: str, shift: int) -> None:
    """Decrypt a text file and write the result to another file."""

    ciphertext = read_text_file(input_path)
    plaintext = decrypt(ciphertext, shift)
    write_text_file(output_path, plaintext)
