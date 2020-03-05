import  numpy as np
import pprint
from solver import  Solver
from printer import  Printer
from matrix import  MatrixOperation
class Maker:
    def __init__(self):
        self.printer = Printer()
        self.pp = pprint.PrettyPrinter()
        self.solver = Solver()
        self.matrix_operation = MatrixOperation()
#Lab1.1
    def make_Lab1_1(self):
        matrix = [
            [1, 2, -2, 6],
            [-3, -5, 14, 13],
            [1, 2, -2, -2],
            [-2, -4, 5, 10],
        ]
        b = [24, 41, 0, 20]
        roots_lup = self.solver.solve_LUP(matrix, b)
        roots_np = np.linalg.solve(matrix, b)
        print('Lab1.1')
        print('Матрица:')
        self.printer.print_matrix(matrix)
        print("Вектор b:")
        self.printer.print_vector(b)
        print("Корни:")
        self.printer.print_roots(roots_lup)
        print('Определитель матрцы')
        det = self.matrix_operation.get_determinant(matrix)
        print(det)
        print('Обратная матрица:')
        matrix_inf = self.matrix_operation.get_inf_matrix(matrix)
        self.printer.print_matrix(matrix_inf)

        # print("Корни при помощи numpy")
        # self.printer.print_roots(roots_np)
        # print('Оперделитель при помощи numpy')
        # print(np.linalg.det(matrix))
        # print('Обратная матрица при помощи numpy')
        # self.printer.print_matrix(np.linalg.inv(matrix))

    # Lab1.2
    def make_Lab1_2(self):
        matrix_sweeps_method = [
            [-11, -9, 0, 0, 0],
            [5, -15, -2, 0, 0],
            [0, -8, 11, -3, 0],
            [0, 0, 6, -15, 4],
            [0, 0, 0, 3, 4]
        ]
        vector_sweeps_method = [-122, -48, -14, -50, 42]

        root_sweeps_method = self.solver.solve_sweeps_methods(matrix_sweeps_method, vector_sweeps_method)
        root_np = np.linalg.solve(matrix_sweeps_method, vector_sweeps_method)
        print('Lab1.2')
        print('Матрица: ')
        self.printer.print_matrix(matrix_sweeps_method)
        print('Вектор b: ')
        self.printer.print_vector(vector_sweeps_method)
        print('Корни: ')
        self.printer.print_roots(root_sweeps_method)
        print('Корни при помощи numpy')
        self.printer.print_roots(root_np)
