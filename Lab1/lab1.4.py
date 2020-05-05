from method_jacobi import get_eigval_eigvec_method_jacobi
from printer import print_eigvals, print_eigvectors
import matplotlib.pyplot as plt
matrix = [
    [0,-7,7],
    [-7,-9,-5],
    [7,-5,-1]
]
print('Собтвенные вектора и собтсвенные значения:\n e = 10^(-5)')
precision = 10**(-5)
eigvals, eigvectors, k = get_eigval_eigvec_method_jacobi(matrix, precision)
print_eigvals(eigvals)
print_eigvectors(eigvectors)
print(f'k = {k}')

import numpy as np
print(f'Проверка {np.dot(matrix,eigvectors[0])} {eigvals[0]*np.array(eigvectors[0])} ')

# precisions = [1/i for i in range(10,100000,10)]
# ks = [get_eigval_eigvec_method_jacobi(matrix, prec)[2] for prec in precisions]
#
# #построение
# fig, ax = plt.subplots(figsize=(5, 3))
# ax.set_title('Зависимость числа итераций от точности')
# ax.set_ylabel('Количесвто итераций')
# ax.set_xlabel('Точность')
# ax.set_xlim(xmin=precisions[0], xmax=precisions[-1])
# ax.plot(precisions,ks)
# fig.tight_layout()
# plt.show()