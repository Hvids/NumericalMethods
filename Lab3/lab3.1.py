import sympy
import numpy as np
from sympy import pi
from copy import deepcopy
from polynom_lagrange import build_lagrange_polynom
from polynom_nuthon import build_nuthon_polynom

x = sympy.symbols('x')

f = sympy.log(x)
vec_x = [0.2,0.6,1,1.4]
x_ = 0.8


L = build_lagrange_polynom(f,x,vec_x)
print('Функция')
sympy.pprint(f)
print(f'Полином Лагранжа')
sympy.pprint(L)
print(f'Значение при X* = {x_}')
print('В полиноме')
print(f'{L.subs(x,x_).evalf()}')
print('В функии')
print(f'{f.subs(x,x_).evalf()}')

print(end='\n\n\n\n')
f = sympy.log(x)
vec_x = [0.2,0.6,1,1.4]
x_ = 0.8
P = build_nuthon_polynom(f,x,vec_x)
print('Функция')
sympy.pprint(f)
print(f'Полином Ньютона')
sympy.pprint(P)
print(f'Значение при X* = {x_}')
print('В полиноме')
print(f'{P.subs(x,x_).evalf()}')
print('В функии')
print(f'{f.subs(x,x_).evalf()}')


output_file_name = "result.json"
res = [L.subs(x,x_).evalf(),P.subs(x,x_).evalf()]
with open(output_file_name,'w') as file:
    file.write(f'{res}')