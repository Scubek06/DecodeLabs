"""Password strength analysis utilities.

This module is intentionally small and readable for a beginner security
project, but the design still follows production habits: pure functions,
clear data models, no password logging, and testable business logic.
"""

from __future__ import annotations

import math
import secrets
import string
from dataclasses import dataclass
from enum import Enum
from getpass import getpass


class Strength(str, Enum):
    """Human-readable password strength labels."""

    WEAK = "Weak"
    MEDIUM = "Medium"
    STRONG = "Strong"


COMMON_WEAK_PASSWORDS = {
    "123456",
    "123456789",
    "12345678",
    "password",
    "qwerty",
    "abc123",
    "111111",
    "123123",
    "admin",
    "letmein",
    "welcome",
    "iloveyou",
    "password1",
}


@dataclass(frozen=True)
class PasswordAnalysis:
    """Complete result returned by the password analyzer."""

    strength: Strength
    score: int
    percentage: int
    entropy_bits: float
    length: int
    has_uppercase: bool
    has_lowercase: bool
    has_digit: bool
    has_special: bool
    is_common_password: bool
    recommendations: tuple[str, ...]


def has_uppercase(password: str) -> bool:
    """Return True when the password contains an uppercase letter."""

    return any(character.isupper() for character in password)


def has_lowercase(password: str) -> bool:
    """Return True when the password contains a lowercase letter."""

    return any(character.islower() for character in password)


def has_digit(password: str) -> bool:
    """Return True when the password contains a numeric digit."""

    return any(character.isdigit() for character in password)


def has_special_character(password: str) -> bool:
    """Return True when the password contains a non-alphanumeric symbol."""

    return any(not character.isalnum() for character in password)


def estimate_character_pool_size(password: str) -> int:
    """Estimate the possible character pool used by a password."""

    pool_size = 0

    if has_lowercase(password):
        pool_size += 26
    if has_uppercase(password):
        pool_size += 26
    if has_digit(password):
        pool_size += 10
    if has_special_character(password):
        pool_size += 33

    return pool_size


def estimate_entropy_bits(password: str) -> float:
    """Estimate password entropy using length and character pool size.

    This is an educational estimate, not a guarantee of real-world resistance.
    Attackers also use leaked password lists, patterns, and user information.
    """

    if not password:
        return 0.0

    pool_size = estimate_character_pool_size(password)
    if pool_size == 0:
        return 0.0

    return len(password) * math.log2(pool_size)


def calculate_score(password: str) -> int:
    """Calculate a 0-100 strength score."""

    if not password:
        return 0

    score = 0
    password_lower = password.lower()

    if len(password) >= 8:
        score += 15
    if len(password) >= 12:
        score += 20
    if len(password) >= 16:
        score += 15

    if has_uppercase(password):
        score += 10
    if has_lowercase(password):
        score += 10
    if has_digit(password):
        score += 10
    if has_special_character(password):
        score += 10

    entropy_bits = estimate_entropy_bits(password)
    if entropy_bits >= 50:
        score += 5
    if entropy_bits >= 70:
        score += 5

    if password_lower in COMMON_WEAK_PASSWORDS:
        score = min(score, 20)

    if len(password) < 8:
        score = min(score, 35)

    if password.isalpha() or password.isdigit():
        score = min(score, 55)

    return max(0, min(score, 100))


def classify_strength(score: int, is_common_password: bool) -> Strength:
    """Convert a numeric score into Weak, Medium, or Strong."""

    if is_common_password or score < 40:
        return Strength.WEAK
    if score < 75:
        return Strength.MEDIUM
    return Strength.STRONG


def build_recommendations(password: str) -> tuple[str, ...]:
    """Return practical recommendations for improving the password."""

    recommendations: list[str] = []

    if not password:
        return ("Enter a password before checking strength.",)

    if len(password) < 12:
        recommendations.append("Use at least 12 characters.")
    if not has_uppercase(password):
        recommendations.append("Add at least one uppercase letter.")
    if not has_lowercase(password):
        recommendations.append("Add at least one lowercase letter.")
    if not has_digit(password):
        recommendations.append("Add at least one number.")
    if not has_special_character(password):
        recommendations.append("Add at least one special character.")
    if password.lower() in COMMON_WEAK_PASSWORDS:
        recommendations.append("Avoid common or leaked passwords.")
    if password.isalpha() or password.isdigit():
        recommendations.append("Avoid using only letters or only numbers.")

    if not recommendations:
        recommendations.append("Good password structure. Store it in a password manager.")

    return tuple(recommendations)


def analyze_password(password: str) -> PasswordAnalysis:
    """Analyze a password and return a structured security result."""

    if password is None:
        raise ValueError("Password cannot be None.")

    normalized_common_check = password.lower()
    is_common = normalized_common_check in COMMON_WEAK_PASSWORDS
    score = calculate_score(password)

    return PasswordAnalysis(
        strength=classify_strength(score, is_common),
        score=score,
        percentage=score,
        entropy_bits=round(estimate_entropy_bits(password), 2),
        length=len(password),
        has_uppercase=has_uppercase(password),
        has_lowercase=has_lowercase(password),
        has_digit=has_digit(password),
        has_special=has_special_character(password),
        is_common_password=is_common,
        recommendations=build_recommendations(password),
    )


def generate_password(length: int = 16) -> str:
    """Generate a strong random password with mixed character classes."""

    if length < 12:
        raise ValueError("Generated passwords should be at least 12 characters long.")

    required_characters = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*()-_=+[]{};:,.?/"),
    ]
    all_characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.?/"
    remaining_characters = [
        secrets.choice(all_characters) for _ in range(length - len(required_characters))
    ]

    password_characters = required_characters + remaining_characters
    secrets.SystemRandom().shuffle(password_characters)
    return "".join(password_characters)


def format_meter(percentage: int, width: int = 20) -> str:
    """Create a text-based strength meter for the command line."""

    filled_blocks = round((percentage / 100) * width)
    empty_blocks = width - filled_blocks
    return f"[{'#' * filled_blocks}{'-' * empty_blocks}] {percentage}%"


def display_analysis(analysis: PasswordAnalysis) -> None:
    """Print a safe password analysis report without revealing the password."""

    print("\nPassword Strength Report")
    print("-" * 28)
    print(f"Strength: {analysis.strength.value}")
    print(f"Score: {analysis.score}/100")
    print(f"Meter: {format_meter(analysis.percentage)}")
    print(f"Estimated entropy: {analysis.entropy_bits} bits")
    print(f"Length: {analysis.length} characters")
    print("\nValidation checks:")
    print(f"- Uppercase letter: {'Yes' if analysis.has_uppercase else 'No'}")
    print(f"- Lowercase letter: {'Yes' if analysis.has_lowercase else 'No'}")
    print(f"- Number: {'Yes' if analysis.has_digit else 'No'}")
    print(f"- Special character: {'Yes' if analysis.has_special else 'No'}")
    print(f"- Common weak password: {'Yes' if analysis.is_common_password else 'No'}")
    print("\nRecommendations:")
    for recommendation in analysis.recommendations:
        print(f"- {recommendation}")


def run_cli() -> None:
    """Run the interactive command-line application."""

    print("Password Strength Checker")
    print("Your password input is hidden and is never stored.")

    try:
        password = getpass("Enter password to analyze: ")
        analysis = analyze_password(password)
        display_analysis(analysis)

        if analysis.strength != Strength.STRONG:
            suggested_password = generate_password()
            print("\nStrong password suggestion:")
            print(suggested_password)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    run_cli()
