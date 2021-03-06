from copy import copy, deepcopy
from matrix import  swap_vector, get_matrix_eye, transporate
from printer import  print_matrix

def LUP_Decomposition(A):
    A = deepcopy(A)
    A = copy(A)
    n = len(A)
    p = [i for i in range(n)]
    k_ = 0
    for k in range(n):
        g = 0
        for i in range(k, n):
            if abs(A[i][k]) > g:
                g = abs(A[i][k])
                k_ = i
        if g == 0:
            raise  NameError("Вырожденная матрица")

        swap_vector(p, k, k_)
        swap_vector(A, k, k_)
        for i in range(k + 1, n):
            A[i][k] = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - A[i][k] * A[k][j]
    return copy(A), copy(p)

def LUP_solve(A, p, b):
    n = len(A)
    X = [0] * n
    Y = [0] * n
    for i in range(n):
        if i == 0:
            y = b[p[i]]
        else:
            sum_y = sum(map(lambda u,y: u*y,A[i][:i],Y[:i]))
            y = b[p[i]] - sum_y
        Y[i] = y
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            X[i] = Y[i] / A[i][i]
        else:
            sum_x = sum(map (lambda l,x: l*x, A[i][i+1:],X[i+1:]))
            X[i] = (Y[i] - sum_x) / A[i][i]
    return copy(X)


def solve_LUP(A, B):
    A = deepcopy(A)
    b = deepcopy(B)
    A, p = LUP_Decomposition(A)
    X = LUP_solve(A, p, b)
    X = list(map(lambda x: round(x,8), X))
    return copy(X)


def devide_LU(A):
    A = deepcopy(A)
    L = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    U = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)):
        L[i][i] =1
        for j in range(len(A)):
            if i > j:
                L[i][j] = A[i][j]
            elif i <= j:
                U[i][j] = A[i][j]
    return L, U

def calc_inv_LU(LU, p):
    n = len(LU)
    E = get_matrix_eye(n)

    res = []
    for i in range(n):
        res.append(LUP_solve(LU,p,E[i]))
    inv_m = transporate(res)
    return inv_m