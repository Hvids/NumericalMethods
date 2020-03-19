import numpy as np
import sympy

def build_lagrange_polynom(f,x,X):
    n = len(X)
    f= [f.subs(x,xi) for xi in X] 
    w = np.prod([(x - xi) for xi in X])
    w_x = [ np.prod([(xi-xj) for xj in X if not xj == xi]) for xi in X ]
    L = sum([ fi*w/((x-xi)*wi_x) for fi,wi_x,xi in zip(f,w_x,X)])
    return L

