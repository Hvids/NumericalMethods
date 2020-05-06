import  sys
sys.path.append('../Lab1/')

import sympy
import numpy as np
from sympy import pi
from methodLUP import solve_LUP

class CubicSplatsn:
    def __init__(self,f_vec, x_vec):
        self.f_vec = f_vec
        self.x_vec = x_vec
        self.size = len(f_vec) - 1
        self.x = sympy.symbols('x')
        self.h_vec = [ x_vec[i+1] - x_vec[i] for i in range(self.size) ]
        self.__create_cubic_splatsn()
    
    def calc_point(self,point):
        k = 0
        for i in range(self.size): 
            if self.x_vec[i]<= point<= self.x_vec[i+1]:
                k = i
        return self.cubic_splatsn[k].subs(self.x,point)
            
    
    def __create_cubic_splatsn(self):
        C, b = self.__create_Cb()
        c_vec = [0] + solve_LUP(C,b)
        a_vec = self.f_vec[:-1]
        b_vec  = [ (self.f_vec[i] - self.f_vec[i-1])/self.h_vec[i-1] -(self.h_vec[i-1]*(c_vec[i] + 2*c_vec[i-1]))/3 for i in range(1,self.size) ] + [ (self.f_vec[-1] - self.f_vec[-2])/self.h_vec[-1] - 2*(self.h_vec[-1]*c_vec[-1])/3 ]
        d_vec = [ (c_vec[i+1]-c_vec[i])/(3*self.h_vec[i]) for i in range(self.size-1) ] + [-c_vec[-1]/(3*self.h_vec[-1])]
        
        self.cubic_splatsn = [ a + b*(self.x-xi)+c*(self.x-xi)**2 + d*(self.x-xi)**3 for i,xi,a,b,c,d, in zip(range(self.size),self.x_vec[:-1],a_vec,b_vec,c_vec,d_vec) ]
    

        
    def __create_Cb(self):
        n = self.size
        h_vec = self.h_vec
        f_vec = self.f_vec
        C = [[2*(h_vec[0] +h_vec[1]), h_vec[1]] + [0]*(n-3)] 
        b = [ 3*( (f_vec[2] - f_vec[1])/h_vec[1] - (f_vec[1] - f_vec[0])/h_vec[0] ) ]
        for i in range(1,n-2):
            row = [0]*(n-1)
            row[i-1] = h_vec[i-1]
            row[i] = 2*(h_vec[i-1] + h_vec[i])
            row[i+1] = h_vec[i]
            C.append(row)
            bI =  3*((f_vec[i+2] - f_vec[i+1])/h_vec[i+1]  - (f_vec[i+1] - f_vec[i])/h_vec[i+1])
            b.append( bI ) 

        b.append( 3*( ( f_vec[-1] -f_vec[-2] )/h_vec[-1] - ( f_vec[-2] - f_vec[-3] )/h_vec[-2] ))

        row = [0]*(n-1)
        row[n-3] = h_vec[n-3]
        row[n-2] = 2*(h_vec[n-3]+h_vec[n-2])
        C.append(row)
        return C, b

if __name__ == '__main__':
    # var 5
    # x_vec = [1,1.9,2.8,3.7,4.6]
    # f_vec = [2.4142,1.0818,0.50953,0.11836,-0.24008]
    x_vec = [0.0, 1.0, 2.0, 3.0, 4.0]
    f_vec = [0.0, 1.8415, 2.9093, 3.1411, 3.2432]
    x_ = 1.5
    cup_sp = CubicSplatsn(f_vec, x_vec)
    for i, sp in enumerate(cup_sp.cubic_splatsn):
        print(f'f{i} = ')
        sympy.pprint(sp)

    f_x_ = cup_sp.calc_point(x_)
    print(f'\nf({x_}) = {f_x_}')
