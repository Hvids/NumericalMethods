import sys
import  numpy as np
sys.path.append('../')
from equation import Equation
from parabolic_solver import ParabolicSolver

import math

eq = Equation(
    f=lambda x, t: 0.5 * np.exp(-0.5 * t) * np.cos(x),
    phi_0=lambda t: -np.exp(-0.5 * t),
    phi_l=lambda t: -np.exp(-0.5 * t),
    psi=lambda x: np.sin(x),
    l=np.pi,
    solution=lambda x, t: np.exp(-0.5 * t) * np.sin(x),
)
solver = ParabolicSolver(
    equation=eq,
    N=10,
    K=10,
    T=10

)
print(solver.solve_analytic()[1])
print('kllkl')
print(solver.solve_crank_nicholson(1)[1])