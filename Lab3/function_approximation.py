import sympy
import numpy as np

class FunctionApproximation:
    def __init__(self,aprox):
        if 3<=aprox <=0:
            raise NameError('Апроксимация должна быть 1 или 2')
        self.aprox = aprox
        self.x_vec = None
        self.f_vec = None
        
    def make(self,f_vec, x_vec):
        self.size = len(f_vec)
        self.x_vec = x_vec
        self.f_vec = f_vec
        self.x = sympy.symbols('x')
        if self.aprox == 1:
            self.__make_fun_aprox1()
        else:
            self.__make_fun_aprox2()
    def diff(self,point,n):
        if 3<= n <= 0:
            raise NameError("Не корретные данные")
        
        if n == 1:
            if self.aprox == 1:
                return self.__diff_one_for_aprox1(point)
            if self.aprox == 2:
                return self.__diff_one_for_aprox2(point)  
        else:
            if self.aprox == 1:
                return self.__diff_two_for_aprox1(point)
            if self.aprox == 2:
                return self.__diff_two_for_aprox2(point)  
                
    def __make_fun_aprox1(self):
        self.phi_vec = [ self.f_vec[i] + (self.f_vec[i+1]-self.f_vec[i])*(self.x - self.x_vec[i])/(self.x_vec[i+1]-self.x_vec[i]) for i in range(self.size-1) ] 
    
    def __diff_one_for_aprox1(self,point):

        diff = []
        for i in range(self.size-1):
            if self.x_vec[i] <= point <= self.x_vec[i+1]:
        
                d = (self.f_vec[i+1]-self.f_vec[i])/(self.x_vec[i+1]-self.x_vec[i])
                diff.append(d)
        return diff
    
    def __diff_two_for_aprox1(self,point):
        raise NameError('Для второй производной использовать многочлен 2-й степени')
    
    def __make_fun_aprox2(self):
        self.__make_fun_aprox1()
        self.phi_vec = self.phi_vec[:-1]
        phi2_vec = [ ( (self.f_vec[i+2] - self.f_vec[i+1])/(self.x_vec[i+2] - self.x_vec[i+1]) - (self.f_vec[i+1] - self.f_vec[i])/(self.x_vec[i+1] - self.x_vec[i]))*(self.x -self.x_vec[i])*(self.x -self.x_vec[i+1])/(self.x_vec[i+2] - self.x_vec[i])    for i in range(self.size - 2)]
        self.phi_vec = list(map(lambda x,y: x+y,self.phi_vec,phi2_vec))
    
    def __diff_one_for_aprox2(self,point):
        diff = []
        for i in range(self.size-2):
            if self.x_vec[i] <=point <= self.x_vec[i+1]:
                d = (self.f_vec[i+1]-self.f_vec[i])/(self.x_vec[i+1]-self.x_vec[i]) + ( (self.f_vec[i+2] - self.f_vec[i+1])/(self.x_vec[i+2] - self.x_vec[i+1]) - (self.f_vec[i+1] - self.f_vec[i])/(self.x_vec[i+1] - self.x_vec[i]) )*(2*point-self.x_vec[i]-self.x_vec[i+1])/(self.x_vec[i+2] - self.x_vec[i])
                diff.append(d)
        return diff
    
    def __diff_two_for_aprox2(self,point):
        diff = []
        for i in range(self.size-2):
            if self.x_vec[i] <=point <= self.x_vec[i+1]:
                d = 2*(
                    (self.f_vec[i+2] - self.f_vec[i+1])/(self.x_vec[i+2] - self.x_vec[i+1]) - (self.f_vec[i+1] - self.f_vec[i])/(self.x_vec[i+1] - self.x_vec[i])
                )/(self.x_vec[i+2] - self.x_vec[i])
                diff.append(d)
        return diff