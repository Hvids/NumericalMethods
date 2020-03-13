from matrix import *
from printer import  *
from method_sweeps import  solve_sweeps_methods
import  numpy as np
matrix_sweeps_method = [
            [-11, -9, 0, 0, 0],
            [5, -15, -2, 0, 0],
            [0, -8, 11, -3, 0],
            [0, 0, 6, -15, 4],
            [0, 0, 0, 3, 4]
]
vector_sweeps_method = [-20, -12, 0, -5, 7]

root_sweeps_method = solve_sweeps_methods(matrix_sweeps_method, vector_sweeps_method)
root_np = np.linalg.solve(matrix_sweeps_method, vector_sweeps_method)
print('Lab1.2')
print('Матрица: ')
print_matrix(matrix_sweeps_method)
print('Вектор b: ')
print_vector(vector_sweeps_method)
print('Корни: ')
print_roots(root_sweeps_method)
print('Корни при помощи numpy')
print_roots(root_np)
