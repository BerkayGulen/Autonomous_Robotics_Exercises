import numpy as np


# Part C
def check_orthogonal(M):

    # I am checking if the input a square matrix
    dim = np.shape(M)[0]
    if dim != np.shape(M)[1]:
        print("input is not a square matrix")
        return
    A = np.dot(M, M.T)
    if np.array_equal(A, np.identity(dim)):
        print("matrix is orthogonal")
    else:
        print("matrix is not orthogonal")


# Part D
M = 1. / 3. * np.array(
    [[2, 2, -1],
     [2, -1, 2],
     [-1, 2, 2]])

check_orthogonal(M)
