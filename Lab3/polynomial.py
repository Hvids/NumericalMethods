import sys
sys.path.append('../Lab1/')

import sympy 
import numpy as np

from methodLUP import solve_LUP

class Polynomial:
    def __init__(self,power):
        self.power = power
        self.count_coeff = power+1
        self.coeff = sympy.symbols(f'a:{self.count_coeff}')
        self.F = None
        self.mse = None
        self.x = None
        
    def make(self, y_vec, x_vec):
        b = []
        A = []
        for k in range(self.count_coeff):
            poly = sum( [ ai*sum([ xj**(k+i) for xj in x_vec]) for i,ai in enumerate(self.coeff) ] )
            E = np.eye(self.count_coeff)
            rowa = [poly.subs(dict(zip(self.coeff,a_vec))) for a_vec in E ]
            A.append(rowa)
            b.append(sum( map( lambda x,y:y*x**k,x_vec,y_vec ) ))
        self.coeff_value = solve_LUP(A,b)
        self.x = sympy.symbols('x')
        x = sympy.symbols('x')
        self.F = sum([ a*x**i for i,a in zip(range(self.count_coeff),self.coeff_value) ])
        self.mse = sum( [ (self.F.subs(x,xi) - yi)**2 for xi,yi in zip(x_vec,y_vec) ] )
        
    
    def calc_point(self,point):
        return self.F.subs(self.x,point)
    
    def print_polynom(self):
        if self.F == None:
            print('Note make')
        else:
            print('F(x) = ')
            sympy.pprint(self.F)
    
    def __get_Ab(self):
        b = []
        A = []
        for k in range(n):
            poly = sum( [ ai*sum([ xj**(k+i) for xj in x_vec]) for i,ai in enumerate(self.coeff) ] )
            E = np.eye(n)
            rowa = [poly.subs(dict(zip(self.coeff,a_vec))) for a_vec in E ]
            A.append(rowa)
            b.append(sum( map( lambda x,y:y*x**k,x_vec,y_vec ) ))
        return A,b