import sympy

def solve_eq_simple_iteration(phi, xstart, q,eps):
    x = sympy.symbols('x')
    k = 0
    while True:
        k += 1
        xk_1 = phi.subs(x,xstart).evalf()
        if q/(1-q)*abs(xstart- xk_1) < eps:
            xstart = xk_1
            break
        else:
            xstart = xk_1
    return xstart, k 
   
    
def solve_eq_method_nuthona(function, eps, xstart):
    x = sympy.symbols('x')
    k = 0
    xk = xstart
    f = function
    df = sympy.diff(f,x)
    e = eps
    while True:
        k+=1
        xk_1 = (xk - (f.subs(x,xk))/(df.subs(x,xk))).evalf()
        if abs(xk_1 - xk) < e:
            xk = xk_1
            break
        else:
            xk = xk_1
    return xk,k