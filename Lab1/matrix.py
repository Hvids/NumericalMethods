import  copy
import  math
class MatrixOperation:
    @staticmethod
    def minor(A, i, j):
        M = copy.deepcopy(A)
        del M[i]
        for i in range(len(A[0]) - 1):
            del M[i][j]
        return M

    @staticmethod
    def get_determinant(A):
        n = len(A[0])
        if n == 1:
            return A[0][0]
        signum = 1
        determinant = 0
        for j in range(n):
            determinant += A[0][j] * signum * MatrixOperation.get_determinant(MatrixOperation.minor(A, 0, j))
            signum *= -1
        return determinant

    @staticmethod
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

    @staticmethod
    def multiplycation_number(number, matrix):
        matrix = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] *= number
        return  matrix
    @staticmethod
    def get_inf_matrix(A):
        A= copy.deepcopy(A)
        det = MatrixOperation().get_determinant(A)
        A_ = []
        for i in range(len(A)):
            row = []
            for j in range(len(A[i])):
                det_minor = MatrixOperation.get_determinant(MatrixOperation.minor(A,i,j))
                a = math.pow(-1.0,i + j + 2)*det_minor
                row.append(a)
            A_.append(row)
        A_ = MatrixOperation.transporate(A_)
        result_matrix = MatrixOperation.multiplycation_number(1/det,A_)
        return result_matrix
