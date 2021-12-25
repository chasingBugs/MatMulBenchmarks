"""Defines tests for the methods implemented in define_methods.py
"""

import unittest

import numpy as np

import define_functions as df


class MultiplicationTests(unittest.TestCase):
    """Implements tests

    Parameters
    ----------
    unittest : Unittest framework
        Automated testing
    """

    def setUp(self):
        self.matrix_a = np.random.rand(5, 7)
        self.matrix_b = np.random.rand(7, 5)
        self.res = np.matmul(self.matrix_a, self.matrix_b)

    def test_python_matmul(self):
        python_res = np.array(df.python_matmul(self.matrix_a, self.matrix_b))
        self.assertTrue(np.allclose(python_res, self.res))

    def test_numpy_matmul(self):
        numpy_res = df.numpy_matmul(self.matrix_a, self.matrix_b)
        self.assertTrue(np.allclose(numpy_res, self.res))

    def test_naive_cython_matmul(self):
        cython_res = df.naive_cython_matmul(self.matrix_a, self.matrix_b)
        self.assertTrue(np.allclose(cython_res, self.res))


if __name__ == '__main__':
    unittest.main()
