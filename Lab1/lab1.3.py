from method_simple_iteration import  solve_simple_iteraion
from method_seidel import solve_mehtod_seidel
from printer import *
import  numpy as np
A = [
    [20,5,7,1],
    [-1,-13,0,-7],
    [4,-6,17,5],
    [-9,8,4,-25]
]
b = [-117,-1,49,-21]
print('Исходная матрица:')
print_matrix(A)
print('Исходный вектор b:')
print_vector(b)

print('Решение методом простых итераций')
X,k = solve_simple_iteraion(A,b)
print_roots(X)
print(f"Количество итераций: {k}")
print("Решение numpy:")
print_roots(np.linalg.solve(A,b))

print("Решение методом Зейделя")
X, k = solve_mehtod_seidel(A,b)
print_roots(X)
print(f"Количество итераций: {k}")

print("Решение numpy:")
print_roots(np.linalg.solve(A,b))
