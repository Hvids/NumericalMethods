from math import atan, sin, cos, pi
from matrix import *
from copy import deepcopy

def get_index_max_abs_elem(matrix):
    l,m = 0,1
    max_abs_elem = matrix[l][m]
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix[i])):
            if max_abs_elem < abs(matrix[i][j]):
                max_abs_elem = abs(matrix[i][j])
                l = i
                m = j
    return l,m
def calc_phi(A, l, m):
    if A[l][l] == A[m][m]:
        return pi/4
    else:
        return 0.5*atan(2*A[l][m]/(A[l][l] - A[m][m]))


def calc_t(matrix):
    sum_t = 0
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix[i])):
            sum_t += matrix[i][j]**2
    sum_t = sum_t**0.5
    return sum_t

def get_eigval_eigvec_method_jacobi(matrix,precision):
    e = precision
    A_k = deepcopy(matrix)
    n = len(A_k)
    U_result = []
    k = -1
    while True:
        k+=1
        l,m = get_index_max_abs_elem(A_k)
        phi = calc_phi(A_k,l,m)
        U = get_matrix_eye(n)
        U[l][m] = -sin(phi)
        U[m][l] = sin(phi)
        U[l][l] = cos(phi)
        U[m][m] = cos(phi)
        U_t = transporate(U)
        A_next  = calc_mult_matrix(calc_mult_matrix(U_t,A_k),U)
        A_k = deepcopy(A_next)
        e_k = calc_t(A_next)
        if k == 0:
            U_result = U
        else:
            U_result = calc_mult_matrix(U_result,U)
        if e_k <= e:
            break
    eigval = [A_k[i][i] for i in range(n)]
    eigvec = [[U_result[i][j] for i in range(len(U_result))] for j in range(len(U_result[0]))]
    return eigval,eigvec, k