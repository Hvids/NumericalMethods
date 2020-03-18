from eigval_qr import get_eigval_qr
from printer import *
import json
def convert_complex_in_arr(vec):
    return list(map(lambda x: [x.real,x.imag],vec))

matrix = [
    [5,8,-2],
    [7,-2,-4],
    [5,8,-1]
]
matrix_complex_eigval = [
    [1, 3, 1],
    [1,1,4],
    [4,3,1]
]
filename = 'test_lab1.5.json'
with open(filename,'r') as file:
    data = json.load(file)

file_out_name = 'output.json'
eigvals = []
for matrix in data:
    print('Матрица:')
    print_matrix(matrix)
    eigval = get_eigval_qr(matrix,10**(-5))
    print_eigvals(eigval)
    eigval = convert_complex_in_arr(eigval)
    eigvals.append(eigval)

with open(file_out_name,'w') as file:
    json.dump(eigvals,file)