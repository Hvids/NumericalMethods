import sympy 
import numpy as np


class Integrator:
    def __init__(self,func,x):
        self.func = func
        self.x = x
    
    def integrate_rectagle(self, a, b, step):
        x_vec, h_vec, f_vec = self.__get_data(a,b,step)
        return sum([ h_vec[i]*self.func.subs(self.x,(x_vec[i-1]+ x_vec[i])/2) for i in range(1,len(x_vec)) ])
    
    
    def integrate_trap(self, a, b, step):
        x_vec, h_vec, f_vec = self.__get_data(a,b,step)
        return 0.5*sum( [ (f_vec[i]+f_vec[i-1])*h_vec[i] for i in range(1,len(x_vec))] )
    
    def integrate_parab(self,a,b,step):
        x_vec, h_vec, f_vec = self.__get_data(a,b,step)
        return sum([ (f_vec[i-1] +  4*self.func.subs(self.x, (x_vec[i] + x_vec[i-1])/2 ) +f_vec[i]  )*h_vec[i]/2 for i in range(1,len(x_vec)) ])/3
    
    
    def clarify_runge(self, Freal, Fh, Fkh, k, p):
        F = Fh +(Fh - Fkh)/(k**p - 1)
        return F, abs(Freal - F).evalf()
    
    def __get_data(self, a, b, step):
        h = step
        x_vec = np.arange(a,b+h/2,h)
        h_vec = [0] + [ x_vec[i] - x_vec[i-1] for i in range(1,len(x_vec))]
        f_vec = [self.func.subs(self.x,xi) for xi in x_vec]
        return x_vec, h_vec, f_vec
        
        
    