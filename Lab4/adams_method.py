from runge_kutta_method import RungeKuttaMethod
from eulera_methods import Method, TableFucntion
from copy import deepcopy
import  numpy as np
import  sympy


class AdamsMethod(Method):
    name = 'Adams Method'
    def __init__(self, step, section):
        Method.__init__(self, step, section)

        if len(np.arange(section[0], section[1], step)) < 4:
            raise NameError('Маленкий шаг')

    def solve(self, func_dict, sdata_dict, ans_vars):
        section = [self.section[0], self.section[0] + 2 * self.step]
        runge_kutta = RungeKuttaMethod(self.step, section)
        table_func, sdata_dict, sdata_list = runge_kutta.solve_for_adams(func_dict, sdata_dict)
        key_func = func_dict.keys()
        a, b, h = section[1] + self.step, self.section[1], self.step
        for _ in np.arange(a, b, h):
            ndata_dict = deepcopy(sdata_dict)

            for key in sdata_dict.keys():
                if key in key_func:

                    ndata_dict[key] = ndata_dict[key] + h * (
                                55 * func_dict[key].subs(sdata_dict) - 59 * func_dict[key].subs(sdata_list[-2]) + 37 *
                                func_dict[key].subs(sdata_list[-3]) - 9 * func_dict[key].subs(sdata_list[-4])) / 24
                else:
                    ndata_dict[key] += h
            sdata_list.append(deepcopy(ndata_dict))
            sdata_dict = deepcopy(ndata_dict)
            for key in sdata_dict.keys():
                table_func[key].append(sdata_dict[key])

        table_func_new = {key: table_func[key] for key in ans_vars}
        var_depend = list(set(ans_vars) & set(func_dict.keys()))
        varibals = list(set(ans_vars) - set(var_depend))
        table_func_dict = TableFucntion(table_func_new, var_depend, varibals)
        return table_func_dict


class AdamsBashfortsMoultonMethod(Method):
    name  = 'Adams Bashforts Moulton Method'

    def __init__(self, step, section):
        Method.__init__(self, step, section)

        if len(np.arange(section[0], section[1], step)) < 4:
            raise NameError('Маленкий шаг')

    def solve(self, func_dict, sdata_dict, ans_vars):
        section = [self.section[0], self.section[0] + 2 * self.step]
        runge_kutta = RungeKuttaMethod(self.step, section)
        table_func, sdata_dict, sdata_list = runge_kutta.solve_for_adams(func_dict, sdata_dict)
        key_func = func_dict.keys()
        a, b, h = section[1] + self.step, self.section[1], self.step
        for _ in np.arange(a, b, h):
            ndata_dict = deepcopy(sdata_dict)

            for key in sdata_dict.keys():
                if key in key_func:

                    ndata_dict[key] = ndata_dict[key] + h * (
                                55 * func_dict[key].subs(sdata_dict) - 59 * func_dict[key].subs(sdata_list[-2]) + 37 *
                                func_dict[key].subs(sdata_list[-3]) - 9 * func_dict[key].subs(sdata_list[-4])) / 24

                else:
                    ndata_dict[key] += h
            sdata_list.append(deepcopy(ndata_dict))

            ndata_dict = deepcopy(sdata_dict)
            for key in sdata_dict.keys():
                if key in key_func:

                    ndata_dict[key] = ndata_dict[key] + h * (
                                9 * func_dict[key].subs(sdata_list[-1]) + 19 * func_dict[key].subs(sdata_list[-2]) - 5 *
                                func_dict[key].subs(sdata_list[-3]) + func_dict[key].subs(sdata_list[-4])) / 24

                else:
                    ndata_dict[key] += h
            sdata_list[-1] = (deepcopy(ndata_dict))
            sdata_dict = deepcopy(ndata_dict)

            for key in sdata_dict.keys():
                table_func[key].append(sdata_dict[key])

        table_func_new = {key: table_func[key] for key in ans_vars}
        var_depend = list(set(ans_vars) & set(func_dict.keys()))
        varibals = list(set(ans_vars) - set(var_depend))
        table_func_dict = TableFucntion(table_func_new, var_depend, varibals)
        return table_func_dict


if __name__ == "__main__":

    from test_data_lab4_1 import  test

    #     test one_order
    parametrs_class_object = test['one_order']['parametrs_class_object']
    parametrs_for_solver = test['one_order']['parametrs_for_solve']
    #   test eem
    method = AdamsMethod(**parametrs_class_object)
    table_func = method.solve(**parametrs_for_solver)
    test_data = test['one_order']['result_last_depend']['am']
    print('am')
    print(f'{table_func.table.tail(1)}  ==  {test_data}')

    method = AdamsBashfortsMoultonMethod(**parametrs_class_object)
    table_func = method.solve(**parametrs_for_solver)
    test_data = test['one_order']['result_last_depend']['abmm']
    print('abmm')
    print(f'{table_func.table.tail(1)}  ==  {test_data}')
