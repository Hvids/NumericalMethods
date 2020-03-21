from copy import deepcopy
from matrix import *

def sign(a):
    if a == 0:
        return 0
    return a/abs(a)


def get_decomposition_qr(matrix):
    n  = len(matrix)
    Ak = deepcopy(matrix)
    Q = get_matrix_eye(n)
    E = get_matrix_eye(n)
    for k in range(n-1):
        V = []
        for i in range(n):
            vi = 0
            if i == k:
                a = Ak[i][k]
                vi = a + sign(a)*calc_norm_row(Ak,k)
            elif i > k:
                vi = Ak[i][k]
            V.append(vi)
        V = transporate([V])
        V_t = transporate(V)
        val_V_tV = calc_mult_matrix(V_t,V)[0][0]
        matrixVV_t = VV_t = calc_mult_matrix(V,V_t)

        H =  calc_diff_matrix(E, calc_mult_val_matrix(2/val_V_tV, matrixVV_t))
        Ak = calc_mult_matrix(H,Ak)
        Q = calc_mult_matrix(Q,H)
    return Q, Ak
