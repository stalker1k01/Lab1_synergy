import unittest
from task7 import pyramid

class TestPyramid(unittest.TestCase):
    def test_succesfull(self):
        successful_values = [1,5,14,30,55]

        for index, value in enumerate(successful_values):
            self.assertEqual(pyramid(value), index)
    
    def test_failed(self):
        failed_values = [2,3,6,8,10,12,23,35,60]
        for index, value in enumerate(failed_values):
            self.assertEqual(pyramid(value), "It is impossible")

    def test_incorrectTypes(self):
        incorrect_inputs = ["string", 1.1]
        for index, value in enumerate(incorrect_inputs):
            self.assertEqual(pyramid(value), "It is impossible")

    def test_negateOrZeroValues(self):
        incorrect_inputs = [-1, 0]
        for index, value in enumerate(incorrect_inputs):
            self.assertEqual(pyramid(value), "It is impossible")