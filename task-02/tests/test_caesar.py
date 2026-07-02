"""Tests for Caesar Cipher encryption and analysis."""

from pathlib import Path
import tempfile
import unittest

from encryption_tool.caesar import (
    ALPHABET_SIZE,
    brute_force,
    calculate_statistics,
    decrypt,
    encrypt,
    frequency_analysis,
    normalize_shift,
)
from encryption_tool.file_crypto import decrypt_file, encrypt_file


class CaesarCipherTests(unittest.TestCase):
    """Validate Caesar Cipher behavior and security learning features."""

    def test_encrypts_uppercase_text(self):
        self.assertEqual(encrypt("HELLO", 3), "KHOOR")

    def test_decrypts_uppercase_text(self):
        self.assertEqual(decrypt("KHOOR", 3), "HELLO")

    def test_preserves_case_spaces_digits_and_symbols(self):
        plaintext = "Decode Labs 2026!"
        ciphertext = encrypt(plaintext, 5)

        self.assertEqual(ciphertext, "Ijhtij Qfgx 2026!")
        self.assertEqual(decrypt(ciphertext, 5), plaintext)

    def test_shift_wraps_at_end_of_alphabet(self):
        self.assertEqual(encrypt("XYZ xyz", 3), "ABC abc")

    def test_large_shift_is_normalized(self):
        self.assertEqual(normalize_shift(29), 3)
        self.assertEqual(encrypt("ABC", 29), "DEF")

    def test_negative_shift_is_supported(self):
        self.assertEqual(encrypt("DEF", -3), "ABC")

    def test_empty_text_is_allowed(self):
        self.assertEqual(encrypt("", 3), "")
        self.assertEqual(decrypt("", 3), "")

    def test_none_text_is_rejected(self):
        with self.assertRaises(ValueError):
            encrypt(None, 3)  # type: ignore[arg-type]

    def test_non_integer_shift_is_rejected(self):
        with self.assertRaises(TypeError):
            encrypt("HELLO", "3")  # type: ignore[arg-type]

    def test_brute_force_returns_all_possible_shifts(self):
        attempts = brute_force("KHOOR")

        self.assertEqual(len(attempts), ALPHABET_SIZE - 1)
        self.assertEqual(attempts[3], "HELLO")

    def test_statistics_counts_character_types(self):
        statistics = calculate_statistics("A b3!")

        self.assertEqual(statistics.total_characters, 5)
        self.assertEqual(statistics.letters, 2)
        self.assertEqual(statistics.digits, 1)
        self.assertEqual(statistics.spaces, 1)
        self.assertEqual(statistics.symbols, 1)

    def test_frequency_analysis_counts_letters_only(self):
        frequencies = frequency_analysis("Attack at dawn! 123")

        self.assertEqual(frequencies["A"], 4)
        self.assertEqual(frequencies["T"], 3)
        self.assertEqual(frequencies["Z"], 0)

    def test_file_encryption_round_trip(self):
        workspace_temp = Path(".test-temp")
        workspace_temp.mkdir(exist_ok=True)

        with tempfile.TemporaryDirectory(dir=workspace_temp) as temporary_directory:
            temp_dir = Path(temporary_directory)
            input_path = temp_dir / "plain.txt"
            encrypted_path = temp_dir / "encrypted.txt"
            decrypted_path = temp_dir / "decrypted.txt"

            input_path.write_text("Secret Message 123!", encoding="utf-8")

            encrypt_file(str(input_path), str(encrypted_path), 4)
            decrypt_file(str(encrypted_path), str(decrypted_path), 4)

            self.assertEqual(decrypted_path.read_text(encoding="utf-8"), "Secret Message 123!")
            self.assertNotEqual(encrypted_path.read_text(encoding="utf-8"), "Secret Message 123!")


if __name__ == "__main__":
    unittest.main()
