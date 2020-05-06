from runge_kutta_method import  RungeKuttaMethod
from condition import  Condition,TYPE_A, TYPE_B
from eulera_methods import  TableFucntion, Method

import  numpy as np
class ShootingMethod(Method):
    name = 'Shooting Method'
    def __init__(self, method_solver, step, eps, section):
        self.method_solver = method_solver(step, section)
        self.step = step
        self.section = section
        self.eps = eps
    def solve(self,func_dict,sdata_dict,ans_vars,cond_a,cond_b,y,dy):
        sdata_dict[y] = cond_a.get_y(1)
        parametrs_for_solve = {
            'func_dict': func_dict,
            'sdata_dict': sdata_dict,
            'ans_vars': ans_vars
        }
        F = []
        n_vec = [1,0.8]
        a,b = self.section
        h = self.step
        i = 0
        table_res = None
        x_vec = np.arange(a,b+h/2,h)
        while True:
            ni = n_vec[i]
            i += 1
            sdata_dict[dy] = ni
            parametrs_for_solve['sdata_dict'] = sdata_dict

            dict_step = self.method_solver.solve_for_shooting(**parametrs_for_solve)
            Fk = cond_b.F(dict_step)
            F.append(Fk)
            epsk = abs(Fk)
            if epsk < self.eps:
                table_res = self.method_solver.solve(**parametrs_for_solve)
                break
            if i > 1:
                n_app = n_vec[-1] - (n_vec[-1] - n_vec[-2])*F[-1]/(F[-1]- F[-2])
                n_vec.append(n_app)

        return table_res


if __name__ == "__main__":
    import  sympy
    import  math
    x, y, z, n = sympy.symbols('x,y,z,n')
    func = {
        y: z,
        z: sympy.exp(x) + sympy.sin(y)
    }
    sdata = {
        x:0,
        y:0,
        z:0,
    }
    section = [0, math.pi/6]
    step = 0.1
    alpha,betta, y_0= (1,0,0)
    delta, gamma, y_1 = (1,0,-math.sqrt(3)/3)
    cond_a = Condition(alpha,betta,y_0, TYPE_A,y, z)
    cond_b = Condition(delta, gamma,y_1, TYPE_B,y, z)
    parametrs_method = {
        'method_solver': RungeKuttaMethod,
        'step':step,
        'eps': 0.0001,
        'section':section
    }
    parametrs_solve = {
        'func_dict':func,
        'sdata_dict':sdata,
        'ans_vars':(x,y),
        'cond_a':cond_a,
        'cond_b':cond_b,
        'dy': z,
        'y':y
    }
    steps = [0.1, 0.05]
    table_fucntions = []
    for step in steps:
        parametrs_method['step'] = step
        method = ShootingMethod(**parametrs_method)
        solution = method.solve(**parametrs_solve)
        table_fucntions.append(solution)
    f_real = -sympy.tan(x)
    print(f'eps Runberga = \n {ShootingMethod.precision_runberg(f_real, table_fucntions[0], table_fucntions[1], 0.5, 2)} ')