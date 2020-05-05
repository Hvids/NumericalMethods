from runge_kutta_method import  RungeKuttaMethod
class ShootingMethod:
    def __init__(self, method_solver, step, eps, section):
        self.method_solver = method_solver
        self.step = step
        self.section = section
        self.eps = eps

    def solve(self, func_dict, sdata_dict, ans_vars, var_z, y_end):

        parametrs_class_obj = {
            'step': self.step,
            'section': self.section
        }

        parametrs_for_solve = {
            'func_dict': func_dict,
            'sdata_dict': sdata_dict,
            'ans_vars': ans_vars
        }

        eps = self.eps
        n_vec = [1, 0.8]
        i = 0
        F = []
        y_vec = []
        table_res = None
        while True:
            ni = n_vec[i]
            i += 1
            sdata_dict[var_z] = ni
            parametrs_for_solve['sdata_dict'] = sdata_dict
            table_k = self.method_solver.solve(**parametrs_for_solve)
            table_res = table_k
            y_ni = table_k.table.iloc[-1, 1]
            y_vec.append(y_ni)
            F.append(y_ni - y_end)
            epsk = abs(y_ni - y_end)
            if epsk < eps:
                break
            if i > 1:
                n_app = n_vec[-1] - (n_vec[-1] - n_vec[-2]) * (F[-1]) / ((F[-1] - F[-2]))
                n_vec.append(n_app)
        return table_res

if __name__ == "__main__":
    import  sympy
    x, y, z, n = sympy.symbols('x,y,z,n')
    y_end = -1.5574077246549023
    func = {
        y: z,
        #     z: sympy.exp(x) + sympy.sin(y)
        z: 2 * (1 + sympy.tan(x) ** 2) * y
    }
    sdata = {
        y: 0,
        z: 0,
        x: 0,
    }
    step = 0.1
    section = [0, 1]
    parametrs_class_obj = {
        'step': step,
        'section': section
    }

    parametrs_methods = {
        'method_solver': RungeKuttaMethod(**parametrs_class_obj),
        'step': step,
        'section': section,
        'eps': 0.0000001
    }
    parametrs_solve = {
        'func_dict': func,
        'sdata_dict': sdata,
        'ans_vars': (x, y),
        'var_z': z,
        'y_end': y_end
    }

    method = ShootingMethod(**parametrs_methods)
    res = method.solve(**parametrs_solve).table
    print(res)