import unittest
import numpy as np
from task3 import get_unique_in_columns, get_unique_in_rows

class testUnique(unittest.TestCase):

    matrix1 = np.array([
            [1,2,2,3],
            [4,4,5,5],
            [3,5,5,5]
        ])

    def test_rows(self):
        rows_result = get_unique_in_rows(self.matrix1)
        expected_rows_result = [np.array([1,2,3]), np.array([4,5]), np.array([3,5])]
        self.assertEqual(rows_result, expected_rows_result)
    
    def test_columns(self):
        columns_result = get_unique_in_columns(self.matrix1)
        expected_columns_result = [np.array([1,4,3]), np.array([2,4,5]), np.array([2,5,5]), np.array([3,5,5])]
        self.assertEqual(columns_result, expected_columns_result)