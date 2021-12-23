"""Defines different methods for matrix multiplication to perform performance
 benchmark tests
"""
import numpy as np


def python_matmul(matrix_a, matrix_b):
    """[summary]

    Parameters
    ----------
    matrix_A : 2D-Iterable
        first matrix
    matrix_B : 2D-Iterable
        second matrix

    Returns
    -------
    2D-Iterable
        multiplication result
    """
    print("Python matrix multiplication started")
    height_a = len(matrix_a)
    height_b = len(matrix_b)

    result = [[0 for i in range(height_a)] for i in range(height_a)]

    for row in range(height_a):
        for column in range(height_a):
            for entry in range(height_b):
                result[row][column] += matrix_a[row][entry] * \
                    matrix_b[entry][column]

    print("Python matrix multiplication ended")

    return result


def numpy_matmul(matrix_a, matrix_b):
    """Simple packaging of numpy matmul

    Parameters
    ----------
    matrix_A : 2D iterable
        A matrix
    matrix_B : 2D iterable
        Another matrix

    Returns
    -------
    2D iterable
        Result matrix
    """
    print("NumPy matmul started")
    res = np.matmul(matrix_a, matrix_b)
    print("NumPy matmul ended")
    return list(res)


def cython_matmul(matrix_a, matrix_b):
    pass
