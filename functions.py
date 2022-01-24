import numpy
import seidel


def LU_Decomposition(matrix):
    A, B = seidel.split(matrix)
    size = len(A)
    L = [[0 for i in range(size)] for j in range(size)]

    for i in range(size):

        # Process L and U
        L[i][i] = 1
        for j in range(i+1, size):
            factor = A[j][i] / A[i][i]
            L[j][i] = factor
            A[j] = [a - b for a, b in zip(A[j], [k * factor for k in A[i]])]

    # Forward Substitution
    D = [0.0 for i in range(size)]
    for i in range(size):
        temp = 0
        for j in range(i):
            temp += D[j]*L[i][j]
        D[i] = B[i] - temp

    # Backward Substitution
    X = [0 for i in range(size)]
    for i in range(size - 1, -1, -1):
        temp = 0
        for j in range(i + 1, size):
            temp += X[j] * A[i][j]
        X[i] = (D[i] - temp) / A[i][i]

    return X


def Gauss_Elimination(A):

    size = len(A)
    for i in range(size):

        # Partial Pivoting
        pivot = i
        for j in range(i + 1, size):
            if A[j][i] > A[pivot][i]:
                pivot = j
        if pivot != i:
            A[pivot], A[i] = A[i], A[pivot]

        # Eliminating
        for j in range(i + 1, size):
            factor = A[j][i] / A[i][i]
            A[j] = [a - b for a, b in zip(A[j], [k * factor for k in A[i]])]

        # # Scaling
        # factor = 1 / A[i][i]
        # A[i] = [k * factor for k in A[i]]

    # Backward Substitution
    X = [0 for i in range(size)]
    for i in range(size - 1, -1, -1):
        temp = 0
        for j in range(i + 1, size):
            temp += X[j] * A[i][j]
        X[i] = (A[i][-1] - temp) / A[i][i]

    return X


def Gauss_Jordan(A):
    size = len(A)
    for i in range(size):

        # Partial Pivoting
        pivot = i
        for j in range(i + 1, size):
            if A[j][i] > A[pivot][i]:
                pivot = j
        if pivot != i:
            A[pivot], A[i] = A[i], A[pivot]

        # Eliminating
        for j in range(size):
            if j == i:
                continue
            factor = A[j][i] / A[i][i]
            A[j] = [a - b for a, b in zip(A[j], [k * factor for k in A[i]])]

        # Scaling
        factor = 1 / A[i][i]
        A[i] = [k * factor for k in A[i]]

    X = [A[i][-1] for i in range(size)]
    return X
