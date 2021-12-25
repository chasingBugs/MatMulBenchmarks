cimport cython


def random_print():
    print('random')


def _naive_cython_matmul(matrix_a, matrix_b):

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


@cython.wraparound(False)
@cython.boundscheck(False)
cpdef _clever_cython_matmul(double[:,:] matrix_a, double[:,:] matrix_b):
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
