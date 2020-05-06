import  sys
sys.path.append('../Lab1/')
from method_sweeps import  solve_sweeps_methods
from condition import Condition, TYPE_A,TYPE_B
from eulera_methods import  TableFucntion, Method
import numpy as np
import  pandas as pd
def insert_start(row, diff):
    for i, d in enumerate(diff):
        row[i] = d
    return row
def insert_end(row, diff):
    for i, d in enumerate(diff):
        row[i-len(diff)] = d
    return row

class FiniteDifferenceMethod(Method):
    name = 'Finite Difference Method'
    def __init__(self,section,step):
        self.section = section
        self.step = step
        self.x_vec = np.arange(section[0],section[1] + step/2,step)
        self.N = round((section[1] - section[0])/step +1)
    def solve(self,p,q,f,cond_a,cond_b,x,y):
        b = []
        matrix = []
        h =self.step
        x_vec = self.x_vec
        N = self.N
        for k in range(self.N):
            row = [0] * N
            xk = x_vec[k]
            if k == 0:
                diff = cond_a.make_diff(h)
                row = insert_start(row, diff)
                b.append(cond_a.rhs)

            if 0 < k < N - 1:
                row[k - 1] = (1 - p(xk) * h / 2)
                row[k] = (-2 + h ** 2 * q(xk))
                row[k + 1] = (1 + p(xk) * h / 2)
                b.append(h ** 2 * f(xk))

            if k == N - 1:
                diff = cond_b.make_diff(h)
                row = insert_end(row, diff)
                b.append(cond_b.rhs)
            matrix.append(row)

        y_res = solve_sweeps_methods(matrix,b)

        table_func_dict = {x:x_vec,y:y_res}

        var_depend = [y]
        varibals = [x]
        table_func_dict = TableFucntion(table_func_dict, var_depend, varibals)
        return table_func_dict

if __name__ == '__main__':
    import  sympy
    def p(x):
        return x
    def q(x):
        return -1
    def f(x):
        return 0
    y,z,x = sympy.symbols('y,z,x')
    section = [0,1]
    count_point = 5
    step = (section[1] - section[0])/count_point
    alpha, betta, y_0 = 1, 0, 1
    delta, gamma, y_1 = 2, 1, 0
    cond_a = Condition(alpha,betta,y_0,TYPE_A,y,z)
    cond_b = Condition(delta,gamma,y_1,TYPE_B,y,z)

    parametrs_method = {
        'step':step,
        'section':section,
    }
    method = FiniteDifferenceMethod(**parametrs_method)
    parametrs_solve ={
        'p':p,
        'f':f,
        'q':q,
        'cond_a':cond_a,
        'cond_b':cond_b,
        'x':x,
        'y':y
    }
    print(method.solve(**parametrs_solve).table)
    print(f'TRUE {[1.0 ,0.77191, 0.58303, 0.43111, 0.31265, 0.22332 ]}')