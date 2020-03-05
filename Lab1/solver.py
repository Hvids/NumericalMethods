from copy import copy, deepcopy

def swap(a, i,j):
    t = a[i]
    a[i] = a[j]
    a[j]= t

class Solver:
    @staticmethod
    def LUP_Decomposition(A):
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

            swap(p, k, k_)
            swap(A, k, k_)
            for i in range(k + 1, n):
                A[i][k] = A[i][k] / A[k][k]
                for j in range(k + 1, n):
                    A[i][j] = A[i][j] - A[i][k] * A[k][j]
        return copy(A), copy(p)
    @staticmethod
    def __LUP_solve(A, p, b):
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

    @staticmethod
    def solve_LUP(A, B):
        A = deepcopy(A)
        b = deepcopy(B)
        A, p = Solver().LUP_Decomposition(A)
        X = Solver().__LUP_solve(A, p, b)
        X = list(map(lambda x: round(x,8), X))
        return copy(X)



    @staticmethod
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