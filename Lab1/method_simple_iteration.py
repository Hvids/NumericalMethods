from copy import  deepcopy
from matrix import *
def solve_simple_iteraion(matrix,vector):
    alpha = get_matrix_alpha(matrix)
    betta = get_vector_betta(matrix, vector)
    X = deepcopy(betta)
    e = 10**(-5)
    k = 0
    norm_alpha = calc_norm_matrix_1(alpha)
    while True:
        k+=1
        X_k = calc_sum_vector(calc_dot_matrix_vector(alpha,X),betta)
        e_k = norm_alpha*(calc_norm_vector(calc_diff_vector(X_k,X)))/(1-norm_alpha)
        if e_k < e:
            break
        else:
            X = deepcopy(X_k)
    return X, k