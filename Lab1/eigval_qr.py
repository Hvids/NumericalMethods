from decomposition_qr import get_decomposition_qr
from copy import deepcopy
from matrix import *
import numpy as np
def get_roots(A, i):
    sz = len(A)
    a11 = A[i][i]
    a12 = A[i][i + 1] if i + 1 < sz else 0
    a21 = A[i + 1][i] if i + 1 < sz else 0
    a22 = A[i + 1][i + 1] if i + 1 < sz else 0
    return np.roots((1, -a11 - a22, a11 * a22 - a12 * a21))

def finish_iter_for_complex(A, eps, i):
    Q, R = get_decomposition_qr(A)
    A_next = calc_mult_matrix(R,Q)
    lambda1 = get_roots(A, i)
    lambda2 = get_roots(A_next, i)
    return True if abs(lambda1[0] - lambda2[0]) <= eps and \
                abs(lambda1[1] - lambda2[1]) <= eps else False


def get_eigenvalue(A, eps, i):
    A_i = deepcopy(A)
    res = 0
    while True:
        Q, R = get_decomposition_qr(A_i)
        A_i = calc_mult_matrix(R, Q)
        if calc_norm_row_d1(A_i, i) <= eps:

            res = (A_i[i][i], False, A_i)
            break
        elif calc_norm_row_d2(A_i, i) <= eps and finish_iter_for_complex(A_i, eps, i):

            res = (get_roots(A_i, i), True, A_i)
            break
    return res

def get_eigval_qr(A, eps):
    res = []
    i = 0
    A_i = deepcopy(A)
    while i < len(A):
        eigenval = get_eigenvalue(A_i, eps, i)
        if eigenval[1]:
            res.extend(eigenval[0])
            i += 2
        else:
            res.append(eigenval[0])
            i += 1
        A_i = eigenval[2]
    return res

