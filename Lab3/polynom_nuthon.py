from copy import deepcopy
import numpy as np
import sympy

def func(f,x,x_vec):
    x_vec = deepcopy(x_vec) 
    if len(x_vec) == 2:
        x1,x2 = tuple(x_vec)
        return (f.subs(x,x1) -f.subs(x,x2))/(x1-x2)
    else:
        return (func(f,x,x_vec[:-1]) - func(f,x,x_vec[1:]) )/(x_vec[0] - x_vec[-1])

    
def build_nuthon_polynom(f,x, vec_x):
    P = 0
    for i in range(len(vec_x)):
        if i == 0:
            P += f.subs(x,vec_x[i])
            continue
        w = np.prod([x - xi for xi in vec_x[:i]])
        P += w*(func(f,x,vec_x[:i+1]).evalf())
    return P
