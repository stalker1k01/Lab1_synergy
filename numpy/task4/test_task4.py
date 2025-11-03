import numpy as np
import matplotlib.pyplot as plt
import unittest
from io import StringIO
import sys
from task4 import analyze_matrix

class TestAnalyzeNormalMatrix(unittest.TestCase):
    
    def setUp(self):
        np.random.seed(42)
        plt.switch_backend('Agg')
    
    def tearDown(self):
        plt.close('all')
    
    def test_matrix_creation_shape_and_type(self):
        m, n = 3, 4
        matrix = analyze_matrix(m, n)
        
        self.assertEqual(matrix.shape, (m, n))
        self.assertEqual(matrix.dtype, np.float64)
    
    def test_edge_cases(self):
        matrix = analyze_matrix(2, 2, mean=5, std=0)
        self.assertTrue(np.allclose(matrix, 5))
        
        matrix_single_row = analyze_matrix(1, 3)
        self.assertEqual(matrix_single_row.shape, (1, 3))
        
        matrix_single_col = analyze_matrix(3, 1)
        self.assertEqual(matrix_single_col.shape, (3, 1))