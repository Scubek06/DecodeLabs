"""Caesar Cipher implementation for educational cryptography.

The Caesar Cipher shifts alphabetic characters by a numeric key. It is useful
for learning encryption logic, but it is not secure for real-world data.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import string


ALPHABET_SIZE = 26


@dataclass(frozen=True)
class TextStatistics:
    """Basic text statistics for encryption analysis."""

    total_characters: int
    letters: int
    digits: int
    spaces: int
    symbols: int


def validate_text(text: str) -> str:
    """Validate text input and return it unchanged."""

    if text is None:
        raise ValueError("Text cannot be None.")
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    return text


def normalize_shift(shift: int) -> int:
    """Validate and normalize a Caesar shift into the range 0-25."""

    if not isinstance(shift, int):
        raise TypeError("Shift key must be an integer.")
    return shift % ALPHABET_SIZE


def shift_character(character: str, shift: int) -> str:
    """Shift one alphabetic character while preserving case."""

    if not character.isalpha() or len(character) != 1:
        return character

    alphabet_start = ord("A") if character.isupper() else ord("a")
    original_position = ord(character) - alphabet_start
    shifted_position = (original_position + shift) % ALPHABET_SIZE
    return chr(alphabet_start + shifted_position)


def encrypt(plaintext: str, shift: int) -> str:
    """Encrypt plaintext with Caesar Cipher."""

    validate_text(plaintext)
    normalized_shift = normalize_shift(shift)
    return "".join(shift_character(character, normalized_shift) for character in plaintext)


def decrypt(ciphertext: str, shift: int) -> str:
    """Decrypt Caesar Cipher text using the original shift key."""

    validate_text(ciphertext)
    normalized_shift = normalize_shift(shift)
    return encrypt(ciphertext, -normalized_shift)


def brute_force(ciphertext: str) -> dict[int, str]:
    """Return every possible Caesar Cipher decryption attempt."""

    validate_text(ciphertext)
    return {shift: decrypt(ciphertext, shift) for shift in range(1, ALPHABET_SIZE)}


def calculate_statistics(text: str) -> TextStatistics:
    """Calculate basic character statistics for a text sample."""

    validate_text(text)
    letters = sum(character.isalpha() for character in text)
    digits = sum(character.isdigit() for character in text)
    spaces = sum(character.isspace() for character in text)
    symbols = len(text) - letters - digits - spaces

    return TextStatistics(
        total_characters=len(text),
        letters=letters,
        digits=digits,
        spaces=spaces,
        symbols=symbols,
    )


def frequency_analysis(text: str) -> dict[str, int]:
    """Count English alphabet letter frequency in a case-insensitive way."""

    validate_text(text)
    normalized_letters = [
        character.upper() for character in text if character.upper() in string.ascii_uppercase
    ]
    counts = Counter(normalized_letters)
    return {letter: counts.get(letter, 0) for letter in string.ascii_uppercase}
