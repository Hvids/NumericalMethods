
def solve_sweeps_methods(A, B):
    """
    lab 1.2
     Метод прогонки.
     Функция находит решение системы уравнений для трех диагональной матрицы
     :param A: Матрица коэфицентов при переменны
     :param B: Вектор свободных значений от переменных
     :return X: Корни линенйного уравнения
    """
    P = [-A[0][1] / A[0][0], ]
    Q = [B[0] / A[0][0], ]
    #  fin coeff of sweeps
    for i in range(1, len(A)):
        if i == len(A) - 1:
            p = 0
        else:
            p = (-A[i][i + 1]) / (A[i][i] + A[i][i - 1] * P[i - 1])
        q = (B[i] - A[i][i - 1] * Q[i - 1]) / (A[i][i] + A[i][i - 1] * P[i - 1])
        P.append(p)
        Q.append(q)

    #  find X
    X = []
    for i in range(len(Q) - 1, -1, -1):
        if i == len(Q) - 1:
            x = Q[i]
        else:
            x = P[i] * X[0] + Q[i]
        X.insert(0, x)
    return X
    A = deepcopy(matrix)
    b = deepcopy(vector)
    A, p = LUP_Decomposition(A)
    X = LUP_solve(A, p, b)
    return copy(X)