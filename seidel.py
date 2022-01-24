import matplotlib.pyplot as plt
import numpy as np


def graph(all_values):
    t = list(range(0, len(all_values)))
    for i in range(len(all_values[0])):
        plt.plot(t, all_values[:, i])
        plt.show()


def split(matrix):
    rows = len(matrix)
    values = []
    coeff = np.full((rows, rows), np.nan)

    for i in range(rows):
        values.append(matrix[i][-1])
        for j in range(rows):
            position = [int(rows * i + j)]
            np.put(coeff, position, float(matrix[i][j]))

    return coeff,values


def gauss_seidel(matrix, results, max_iterations, eps):
    coefficients,values = split(matrix)
    rows = len(coefficients)

    all_values = np.full((max_iterations, rows), np.nan)

    for k in range(0, max_iterations):

        for i in range(rows):
            results[i] = values[i]
            position = [int(rows * k + i)]
            np.put(all_values, position, results[i])
            for j in range(rows):
                if i == j:
                    continue
                results[i] = results[i] - coefficients[i][j] * results[j]

            results[i] = results[i] / coefficients[i][i]
            position = [int(rows * k + i)]
            np.put(all_values, position, results[i])

        flag = 0
        for v in range(rows):
            if abs(all_values[k - 1][0] - all_values[k][0]) / all_values[k - 1][0] <= eps:
                flag = flag + 1
        if flag == rows:
            break

    graph(all_values)
    return results
