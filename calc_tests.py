# Hayden Knapp
#
# Test features of the calc module using unittests

import unittest

import calc

class CalcUnitTests(unittest.TestCase):
    def test_001_single_digit_2(self):
        self.assertEqual(calc.evaluate_single_digit("2"), 2)

    def test_002_single_digit_9(self):
        self.assertEqual(calc.evaluate_single_digit("9"), 9)

    def test_003_single_digit_0(self):
        self.assertEqual(calc.evaluate_single_digit("0"), 0)

    def test_004_positive_numbers_142(self):
        self.assertEqual(calc.evaluate_positive_number("142"), 142)

    def test_005_positive_numbers_9(self):
        self.assertEqual(calc.evaluate_positive_number("9"), 9)

    def test_006_floating_point_9_dec(self):
        self.assertEqual(calc.evaluate_floating_point_number("9"), 9)

    def test_007_floating_point_9_float(self):
        self.assertEqual(calc.evaluate_floating_point_number("9.0"), 9.0)

    def test_008_floating_point_1357246_1902_float(self):
        self.assertEqual(calc.evaluate_floating_point_number("1357246.1902"), 1357246.1902)

    def test_009_single_hex_6(self):
        self.assertEqual(calc.evaluate_single_hexadecimal_digit("6"), 6)

    def test_010_single_hex_F(self):
        self.assertEqual(calc.evaluate_single_hexadecimal_digit("F"), 15)

    def test_011_single_hex_F9(self):
        self.assertEqual(calc.evaluate_hexadecimal("F9"), 249)

    def test_012_single_hex_123(self):
        self.assertEqual(calc.evaluate_hexadecimal("123"), 291)

    def test_012_single_hex_123(self):
        self.assertEqual(calc.evaluate_hexadecimal("123"), 291)

    def test_013_single_hex_8DEF123(self):
        self.assertEqual(calc.evaluate_hexadecimal("8DEF123"), 148828451)

if __name__ == "__main__":
    unittest.main(verbosity=2);
