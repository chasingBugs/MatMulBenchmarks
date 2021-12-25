"""A script to run and test the developed matrix multiplication methods
"""
import numpy as np

import define_functions


def main():
    matrix_a = np.random.rand(5, 7)
    matrix_b = np.random.rand(7, 5)

    # test_matrix_A = [[2, 1, 0], [0, 2, 0], [0, 0, 2]]
    # test_matrix_B = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]

    # my_list = [[0 for i in range(10)] for i in range(10)]
    # my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print(my_list)

    mul_result = define_functions.naive_cython_matmul(matrix_a, matrix_b)
    print(mul_result)


if __name__ == "__main__":
    main()
