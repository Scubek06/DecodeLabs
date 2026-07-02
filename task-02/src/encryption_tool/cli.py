"""Menu-driven command-line interface for the encryption tool."""

from __future__ import annotations

import logging

from encryption_tool.caesar import (
    brute_force,
    calculate_statistics,
    decrypt,
    encrypt,
    frequency_analysis,
)
from encryption_tool.file_crypto import decrypt_file, encrypt_file


LOG_FILE = "encryption_tool.log"


def configure_logging() -> None:
    """Configure application logging without recording sensitive user text."""

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def read_shift() -> int:
    """Read and validate a numeric shift key from the user."""

    raw_shift = input("Enter shift key as an integer: ").strip()
    try:
        return int(raw_shift)
    except ValueError as error:
        raise ValueError("Shift key must be a valid integer.") from error


def print_statistics(text: str) -> None:
    """Display text statistics and frequency analysis."""

    statistics = calculate_statistics(text)
    frequencies = frequency_analysis(text)

    print("\nEncryption Statistics")
    print("-" * 25)
    print(f"Total characters: {statistics.total_characters}")
    print(f"Letters: {statistics.letters}")
    print(f"Digits: {statistics.digits}")
    print(f"Spaces: {statistics.spaces}")
    print(f"Symbols: {statistics.symbols}")

    print("\nLetter Frequency")
    print("-" * 25)
    for letter, count in frequencies.items():
        if count:
            print(f"{letter}: {count}")


def handle_encrypt() -> None:
    """Encrypt user-provided text."""

    plaintext = input("Enter plaintext: ")
    shift = read_shift()
    ciphertext = encrypt(plaintext, shift)
    logging.info("Encrypted text using Caesar Cipher.")
    print(f"\nEncrypted output: {ciphertext}")


def handle_decrypt() -> None:
    """Decrypt user-provided text."""

    ciphertext = input("Enter ciphertext: ")
    shift = read_shift()
    plaintext = decrypt(ciphertext, shift)
    logging.info("Decrypted text using Caesar Cipher.")
    print(f"\nDecrypted output: {plaintext}")


def handle_brute_force() -> None:
    """Show every Caesar Cipher shift attempt."""

    ciphertext = input("Enter ciphertext to brute force: ")
    attempts = brute_force(ciphertext)
    logging.info("Ran Caesar brute-force demonstration.")

    print("\nBrute-force Results")
    print("-" * 25)
    for shift, plaintext in attempts.items():
        print(f"Shift {shift:2}: {plaintext}")


def handle_statistics() -> None:
    """Analyze user-provided text."""

    text = input("Enter text to analyze: ")
    logging.info("Calculated encryption statistics.")
    print_statistics(text)


def handle_file_encryption(encrypt_mode: bool) -> None:
    """Encrypt or decrypt a UTF-8 text file."""

    input_path = input("Enter input file path: ").strip()
    output_path = input("Enter output file path: ").strip()
    shift = read_shift()

    if encrypt_mode:
        encrypt_file(input_path, output_path, shift)
        logging.info("Encrypted a text file.")
        print(f"Encrypted file written to: {output_path}")
    else:
        decrypt_file(input_path, output_path, shift)
        logging.info("Decrypted a text file.")
        print(f"Decrypted file written to: {output_path}")


def show_menu() -> None:
    """Display the available application actions."""

    print("\nBasic Encryption & Decryption")
    print("-" * 31)
    print("1. Encrypt text")
    print("2. Decrypt text")
    print("3. Brute-force Caesar cipher")
    print("4. Show encryption statistics")
    print("5. Encrypt text file")
    print("6. Decrypt text file")
    print("7. Exit")


def main() -> None:
    """Run the menu-driven command-line application."""

    configure_logging()

    actions = {
        "1": handle_encrypt,
        "2": handle_decrypt,
        "3": handle_brute_force,
        "4": handle_statistics,
        "5": lambda: handle_file_encryption(encrypt_mode=True),
        "6": lambda: handle_file_encryption(encrypt_mode=False),
    }

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "7":
            logging.info("User exited the application.")
            print("Goodbye.")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid option. Choose a number from 1 to 7.")
            continue

        try:
            action()
        except (FileNotFoundError, TypeError, ValueError) as error:
            logging.warning("Handled user input error: %s", error)
            print(f"Error: {error}")
        except OSError as error:
            logging.error("File operation failed: %s", error)
            print(f"File error: {error}")


if __name__ == "__main__":
    main()
