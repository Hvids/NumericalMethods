from matrix import *
from printer import  *
from methodLUP import  solve_LUP
import  numpy as np
matrix = [
    [1, 2, -2, 6],
    [-3, -5, 14, 13],
    [1, 2, -2, -2],
    [-2, -4, 5, 10],
]
b = [24, 41, 0, 20]
roots_lup = solve_LUP(matrix, b)
roots_np = np.linalg.solve(matrix, b)
print('Lab1.1')
print('Матрица:')
print_matrix(matrix)
print("Вектор b:")
print_vector(b)
print("Корни:")
print_roots(roots_lup)


print('Определитель матрцы')
det = calc_determinant(matrix)
print(det)
print('Обратная матрица:')

matrix_inf = calc_inv_matrix(matrix)
print_matrix(matrix_inf)

# print("Корни при помощи numpy")
# print_roots(roots_np)
# print('Оперделитель при помощи numpy')
# print(np.linalg.det(matrix))
# print('Обратная матрица при помощи numpy')
# print_matrix(np.linalg.inv(matrix))
