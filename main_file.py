'''A script to run and test the developed matrix multiplication methods
'''
import numpy as np
import define_functions


def main():
    heigth = 100
    width = 100
    matrix_A = np.random.rand(5, 7)
    matrix_B = np.random.rand(7, 5)

    #test_matrix_A = [[2, 1, 0], [0, 2, 0], [0, 0, 2]]
    #test_matrix_B = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]

    #my_list = [[0 for i in range(10)] for i in range(10)]
    #my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print(my_list)

    mul_result = define_functions.normal_python_multiply_matrix(matrix_A, matrix_B)
    print(mul_result)
    
    
if __name__ == '__main__':
    main()

