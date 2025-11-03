import unittest
from task8 import is_balanced_number

class testBalance(unittest.TestCase):
    def test_single_digit(self):
        self.assertTrue(is_balanced_number(1))
        self.assertTrue(is_balanced_number(9))
        self.assertTrue(is_balanced_number(0))
    
    def test_two_digits(self):
        self.assertTrue(is_balanced_number(12))
        self.assertTrue(is_balanced_number(99))
        self.assertTrue(is_balanced_number(10))
    
    def test_balanced(self):
        self.assertTrue(is_balanced_number(121))
        self.assertTrue(is_balanced_number(12321))
        self.assertTrue(is_balanced_number(10203))
    
    def test_unbalanced(self):
        self.assertFalse(is_balanced_number(123))
        self.assertFalse(is_balanced_number(12345))
        self.assertFalse(is_balanced_number(10234))
    
    def test_length_balanced(self):
        self.assertTrue(is_balanced_number(1221))
        self.assertTrue(is_balanced_number(123321))
        self.assertTrue(is_balanced_number(1001))
    
    def test_length_unbalanced(self):
        self.assertFalse(is_balanced_number(1234))
        self.assertFalse(is_balanced_number(123456))
        self.assertFalse(is_balanced_number(1002))