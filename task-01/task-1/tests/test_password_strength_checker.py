"""Unit tests for the Password Strength Checker project."""

import unittest

from password_strength_checker import (
    Strength,
    analyze_password,
    estimate_entropy_bits,
    generate_password,
)


class PasswordStrengthCheckerTests(unittest.TestCase):
    """Test password analysis behavior and important security edge cases."""

    def test_empty_password_is_weak(self):
        analysis = analyze_password("")

        self.assertEqual(analysis.strength, Strength.WEAK)
        self.assertEqual(analysis.score, 0)
        self.assertIn("Enter a password", analysis.recommendations[0])

    def test_common_password_is_weak_even_with_some_rules(self):
        analysis = analyze_password("password1")

        self.assertEqual(analysis.strength, Strength.WEAK)
        self.assertTrue(analysis.is_common_password)
        self.assertLessEqual(analysis.score, 20)

    def test_short_mixed_password_is_not_strong(self):
        analysis = analyze_password("Aa1!")

        self.assertEqual(analysis.strength, Strength.WEAK)
        self.assertIn("Use at least 12 characters.", analysis.recommendations)

    def test_medium_password_classification(self):
        analysis = analyze_password("Decode2026")

        self.assertEqual(analysis.strength, Strength.MEDIUM)
        self.assertFalse(analysis.has_special)

    def test_strong_password_classification(self):
        analysis = analyze_password("D3c0deLabs!2026")

        self.assertEqual(analysis.strength, Strength.STRONG)
        self.assertGreaterEqual(analysis.score, 75)
        self.assertGreater(analysis.entropy_bits, 70)

    def test_entropy_increases_with_length(self):
        short_entropy = estimate_entropy_bits("Ab1!")
        long_entropy = estimate_entropy_bits("Ab1!Ab1!Ab1!Ab1!")

        self.assertGreater(long_entropy, short_entropy)

    def test_generated_password_meets_minimum_security_rules(self):
        generated_password = generate_password(16)
        analysis = analyze_password(generated_password)

        self.assertEqual(len(generated_password), 16)
        self.assertTrue(analysis.has_uppercase)
        self.assertTrue(analysis.has_lowercase)
        self.assertTrue(analysis.has_digit)
        self.assertTrue(analysis.has_special)

    def test_generator_rejects_short_lengths(self):
        with self.assertRaises(ValueError):
            generate_password(8)

    def test_none_password_rejected(self):
        with self.assertRaises(ValueError):
            analyze_password(None)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
