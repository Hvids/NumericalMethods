from matrix import *
from copy import  deepcopy
def solve_mehtod_seidel(matrix,vector):
    alpha = get_matrix_alpha(matrix)
    betta = get_vector_betta(matrix,vector)
    B = get_matrixB(alpha)
    C = get_mareixC(alpha)
    E = get_matrixE(len(B))
    X = deepcopy(betta)
    e = 10**(-5)
    norm_C = calc_norm_matrix_1(C)
    norm_alpha = calc_norm_matrix_1(alpha)
    k = 0
    while True:
        k+=1
        E_B = calc_inv_matrix(calc_diff_matrix(E,B))
        E_BC = calc_mult_matrix(E_B,C)
        X_k=calc_sum_vector( calc_dot_matrix_vector(E_BC,X),calc_dot_matrix_vector(E_B,betta))
        e_k = norm_C*(calc_norm_vector(calc_diff_vector(X,X_k)))/(1-norm_alpha)
        X = deepcopy(X_k)
        if e_k<e:
            break
    return X,k