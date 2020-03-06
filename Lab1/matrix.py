import  copy
import  math

def swap_vector(a, i,j):
    t = a[i]
    a[i] = a[j]
    a[j]= t



def minor(A, i, j):
    M = copy.deepcopy(A)
    del M[i]
    for i in range(len(A[0]) - 1):
        del M[i][j]
    return M


def calc_determinant(A):
    n = len(A[0])
    if n == 1:
        return A[0][0]
    signum = 1
    determinant = 0
    for j in range(n):
        determinant += A[0][j] * signum * calc_determinant(minor(A, 0, j))
        signum *= -1
    return determinant


def transporate(A):
    A = copy.deepcopy(A)
    M = []
    n = len(A[0])
    for j in range(len(A[0])):
        row = []
        for i in range(len(A)):
          row.append(A[i][j])
        M.append(row)
    return  M


def multiplycation_number(number, matrix):
    matrix = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= number
    return  matrix

def calc_mult_matrix(m1, m2):
    s = 0  # сумма
    t = []  # временная матрица
    m3 = []  # конечная матрица
    if len(m2) != len(m1[0]):
        print ("Матрицы не могут быть перемножены")
    else:
        r1 = len(m1)  # количество строк в первой матрице
        c1 = len(m1[0])  # Количество столбцов в 1
        r2 = c1  # и строк во 2ой матрице
        c2 = len(m2[0])  # количество столбцов во 2ой матрице
        for z in range(0, r1):
            for j in range(0, c2):
                for i in range(0, c1):
                    s = s + m1[z][i] * m2[i][j]
                t.append(s)
                s = 0
            m3.append(t)
            t = []
    return m3


def calc_inv_matrix(A):
    A= copy.deepcopy(A)
    det = calc_determinant(A)
    A_ = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            det_minor = calc_determinant(minor(A,i,j))
            a = math.pow(-1.0,i + j + 2)*det_minor
            row.append(a)
        A_.append(row)
    A_ = transporate(A_)
    result_matrix = multiplycation_number(1/det,A_)
    return result_matrix

# for lab1.3
def get_matrix_alpha(matrix):
    alpha = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            if not i == j:
                a = -matrix[i][j]/matrix[i][i]
                row.append(a)
            else:
                row.append(0)
        alpha.append(row)
    return alpha

def get_vector_betta(matrix,b):
    betta = []
    for i in range(len(matrix)):
        bt= b[i]/matrix[i][i]
        betta.append(bt)
    return betta

def get_matrixB(matrix):
    B = []
    for i in range(len(matrix)):
        row = [0]*len(matrix[i])
        for j in range(len(matrix[i])):
            if i > j:
                row[j] = matrix[i][j]
            else:
                row[j] = 0
        B.append(row)
    return B

def get_mareixC(matrix):
    C = []
    for i in range(len(matrix)):
        row = [0] * len(matrix[i])
        for j in range(len(matrix[i])):
            if i < j:
                row[j] = matrix[i][j]
            else:
                row[j] = 0
        C.append(row)
    return C

def get_matrixE(n):
    result = []
    for i in range(n):
        row = [0]*n
        row[i] = 1
        result.append(row)
    return result
# конец специальных матри


# маскимальная сумма по строкам
def calc_norm_matrix_c(matrix):
    n = len(matrix)
    max_sum = 0
    for i in range(n):
        row_abs = map(abs, matrix[i])
        sum_row = sum(row_abs)
        max_sum = max(sum_row,max_sum)
    return max_sum

# корень квадратный из суммы всех элементов
def calc_norm_matrix_2(matrix):
    norm = 0
    for row in matrix:
        for value in row:
            norm += value**2
    norm = norm**0.5
    return norm

# максимальная сумма по столбцам
def calc_norm_matrix_1(matrix):
    n = len(matrix)
    norm = 0
    for j in range(len(matrix[0])):
        row_sum = 0
        for i in range(len(matrix)):
            row_sum += abs(matrix[i][j])
        norm = max(row_sum,norm)
    return norm

def calc_norm_vector(vector):
    norm = 0
    for value in vector:
        norm += value**2
    norm = norm**(0.5)
    return norm


def calc_dot_matrix_vector(matrix, vector):
    result = [0] * len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i] += matrix[i][j] * vector[j]
    return result


def calc_sum_matrix(m1, m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result


def calc_diff_matrix(m1, m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] - m2[i][j])
        result.append(row)
    return result


def calc_sum_vector(rhs, lhs):
    result = [0] * len(rhs)
    for i in range(len(rhs)):
        result[i] += rhs[i] + lhs[i]
    return result


def calc_diff_vector(rhs, lhs):
    result = [0] * len(rhs)
    for i in range(len(rhs)):
        result[i] += rhs[i] - lhs[i]
    return result