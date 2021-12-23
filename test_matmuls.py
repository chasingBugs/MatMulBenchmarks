'''Defines tests for the methods implemented in define_methods.py
'''

import unittest
import numpy as np
import define_functions as df


class MultiplicationTests(unittest.TestCase):
    '''Implements tests

    Parameters
    ----------
    unittest : Unittest framework
        Automated testing
    '''
    def setUp(self):
        self.matrix_A = np.random.rand(5, 7)
        self.matrix_B = np.random.rand(7, 5)
        self.res = np.matmul(self.matrix_A, self.matrix_B)

    def test_python_matmul(self):
        python_res = np.array(df.python_matmul(self.matrix_A, self.matrix_B))
        self.assertTrue(np.allclose(python_res, self.res))

    def test_numpy_matmul(self):
        numpy_res = df.numpy_matmul(self.matrix_A, self.matrix_B)
        self.assertTrue(np.allclose(numpy_res, self.res))


    