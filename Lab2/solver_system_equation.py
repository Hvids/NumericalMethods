import sys
sys.path.append('../Lab1/')

import sympy
from copy import deepcopy
from matrix import calc_determinant

class Jacobian:
    def __init__(self,f_vector,x_vector):
        self.f_vector = f_vector
        self.x_vector = x_vector
        self.__create_jacobian()

    def __create_jacobian(self):
        J = []
        for f in self.f_vector:
            drow = []
            for t in self.x_vector:
                df = sympy.diff(f, t)
                drow.append(df)
            J.append(drow)
        self.jacobian = J
    
    def calc_point(self,xk):
        x = dict(zip(self.x_vector,xk))
        J = deepcopy(self.jacobian)
        n, m = len(J), len(J[0])
        for i in range(n):
            for j in range(m):
                J[i][j] = J[i][j].subs(x)
        return J
    
    def calc_det_point(self,xk):
        J_p = self.calc_point(xk)
        return calc_determinant(J_p)

class ListMatrixA:
    def __init__(self,f_vector,x_vector):
        self.f_vector = f_vector
        self.x_vector = x_vector
        self.__create_list_matrix()
        
    def __create_list_matrix(self):
        x_size = len(self.x_vector)
        A = []
        for x_ind in range(x_size):
            A_i = []
            for row_index in range(x_size):
                row = []
                for col_index in range(x_size):
                    if x_ind == col_index:
                        row.append(self.f_vector[row_index])
                    else:
                        row.append(sympy.diff(self.f_vector[row_index], self.x_vector[col_index]))
                A_i.append(row)
            A.append(A_i)
        self.list_matrix = A
    def calc_point(self, xk):
        x = dict(zip(self.x_vector,xk))
        A = deepcopy(self.list_matrix)
        for mi in range(len(A)):
            for i in range(len(A[mi])):
                for j in range(len(A[mi][i])):
                    A[mi][i][j] = A[mi][i][j].subs(x)
        return A 
    
    def calc_det_point(self,xk):
        A_point = self.calc_point(xk)
        det = [calc_determinant(Ak) for Ak in A_point]
        return det
    
    
def calc_eps_root(xstart, xnext):
    return max(map(lambda x,y: abs(x-y), xstart,xnext))

class MethodNuthona:
    def __init__(self,f_vector,x_vector):
        self.f_vector = f_vector
        self.x_vector = x_vector
        self.root = None
        self.count_iteration = None
    def solve(self, xstart, eps=0.0001):
        J = Jacobian(self.f_vector,self.x_vector)
        ListA = ListMatrixA(self.f_vector,self.x_vector)
        k=0
        while True:
            k += 1
            xnext = []
            dets_A_point = ListA.calc_det_point(xstart)
            det_J_point = J.calc_det_point(xstart)
            for det_A_point,x_i in zip(dets_A_point, xstart):
                xnext_i = x_i - det_A_point/det_J_point
                xnext.append(xnext_i)
            epsk = calc_eps_root(xnext,xstart)
            xstart = xnext
            if epsk < eps:
                break
        self.root = xstart
        self.count_iteration = k
        return xstart, k

class SimpleIteration:
    def  __init__(self,phi, x_vector):
        self.phi = phi
        self.x_vector = x_vector
    def solve(self,xstart, q = 0.999, eps = 0.00001):
        k = 0
        while True:
            k += 1
          
            xk = dict(zip(self.x_vector,xstart))
            
            xnext = list( map(lambda p: p.subs(xk), self.phi))
            
            epsk = q*calc_eps_root(xstart,xnext)/(1-q)
            xstart = xnext
            if epsk < eps:
                break
        return xstart, k
