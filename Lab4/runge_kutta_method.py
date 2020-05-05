from eulera_methods import Method, TableFucntion
from copy import deepcopy
import  numpy as np
import  sympy
import  pandas as pd


class RungeKuttaMethod(Method):
    def solve(self, func_dict, sdata_dict, ans_vars):
        order_of_preciosion = 4
        h = self.step
        a, b = self.section
        sdata_dict = deepcopy(sdata_dict)
        table_func_dict = {key: [sdata_dict[key]] for key in ans_vars}
        key_func = func_dict.keys()
        for i in np.arange(a, b, h):

            # print(i)
            #             dy
            delta_function = {key: 0 for key in func_dict}
            #             K
            coeff_dict = {key: 0 for key in func_dict}

            for j in range(order_of_preciosion):
                # print(j)

                ndata_dict = deepcopy(sdata_dict)

                for key in sdata_dict.keys():
#                     print(key)
                    if key in key_func:
#                         print(key) 
                        if j == 0:
                            ndata_dict[key] = sdata_dict[key]

                        elif 0 < j < order_of_preciosion - 1:
                            ndata_dict[key] = sdata_dict[key] +  coeff_dict[key] / 2

                        else:
                            ndata_dict[key] = sdata_dict[key] +  coeff_dict[key]

                    else:

                        if j == 0:
                            ndata_dict[key] = sdata_dict[key]

                        elif 0 < j < order_of_preciosion - 1:
                            ndata_dict[key] = sdata_dict[key] + h / 2
                        else:
                            ndata_dict[key] = sdata_dict[key] + h

                for key in key_func:
                    coeff_dict[key] = h * func_dict[key].subs(ndata_dict).evalf()

                    delta_function[key] = delta_function[key] + coeff_dict[
                        key] if j == 0 or j == order_of_preciosion - 1 else delta_function[key] + 2 * coeff_dict[key]

            for key in sdata_dict.keys():
                if key in key_func:
                    sdata_dict[key] = sdata_dict[key] + delta_function[key] / 6
                else:
                    sdata_dict[key] += h
            for key in ans_vars:
                table_func_dict[key].append(sdata_dict[key])

        var_depend = list(set(ans_vars) & set(func_dict.keys()))
        varibals = list(set(ans_vars) - set(var_depend))
        table_func_dict = TableFucntion(table_func_dict, var_depend, varibals)
        return table_func_dict

    def solve_for_adams(self,func_dict, sdata_dict):
        order_of_preciosion = 4
        h = self.step
        a, b = self.section
        sdata_dict = deepcopy(sdata_dict)

        sdata_list = [deepcopy(sdata_dict)]
        table_func_dict = {key: [sdata_dict[key]] for key in sdata_dict.keys()}
        key_func = func_dict.keys()

        for i in np.arange(a, b, h):
            #             dy
            delta_function = {key: 0 for key in func_dict}
            #             K
            coeff_dict = {key: 0 for key in func_dict}

            for j in range(order_of_preciosion):

                ndata_dict = deepcopy(sdata_dict)

                for key in sdata_dict.keys():
                    if key in key_func:

                        if j == 0:
                            ndata_dict[key] = sdata_dict[key]

                        elif 0 < j < order_of_preciosion - 1:
                            ndata_dict[key] = sdata_dict[key] + coeff_dict[key] / 2

                        else:
                            ndata_dict[key] = sdata_dict[key] + coeff_dict[key]

                    else:

                        if j == 0:
                            ndata_dict[key] = sdata_dict[key]

                        elif 0 < j < order_of_preciosion - 1:
                            ndata_dict[key] = sdata_dict[key] + h / 2
                        else:
                            ndata_dict[key] = sdata_dict[key] + h

                for key in key_func:
                    coeff_dict[key] = h * func_dict[key].subs(ndata_dict).evalf()

                    delta_function[key] = delta_function[key] + coeff_dict[
                        key] if j == 0 or j == order_of_preciosion - 1 else delta_function[key] + 2 * coeff_dict[key]

            for key in sdata_dict.keys():
                if key in key_func:
                    sdata_dict[key] = sdata_dict[key] + delta_function[key] / 6
                else:
                    sdata_dict[key] += h

            sdata_list.append(deepcopy(sdata_dict))
            for key in sdata_dict.keys():
                table_func_dict[key].append(sdata_dict[key])

        return table_func_dict, sdata_dict, sdata_list

    def solve_for_shooting(self,func_dict, sdata_dict,ans_vars):
        table,_,_ = self.solve_for_adams(func_dict,sdata_dict)
        table = pd.DataFrame(table)
        table = table[ans_vars]
        return table

        return

if __name__ == '__main__':
    x, y, z, n = sympy.symbols('x,y,z,n')
    func = {
        y: z,
        z: sympy.exp(x) + sympy.sin(y)
    }
    sdata = {
        y: 1,
        z: 1,
        x: 0,
    }
    step = 0.15
    import  math
    section = [0, math.pi/6]

    parametrs_class_obj = {
        'step': step,
        'section': section
    }
    parametrs_for_solve = {
        'func_dict': func,
        'sdata_dict': sdata,
        'ans_vars': [x, y]
    }
    method = RungeKuttaMethod(**parametrs_class_obj)
    t= method.solve_for_shooting(**parametrs_for_solve)

    print(t)
    # from test_data_lab4_1 import test
    #
    # #     test one_order
    # parametrs_class_object = test['one_order']['parametrs_class_object']
    # parametrs_for_solver = test['one_order']['parametrs_for_solve']
    # #   test
    # method = RungeKuttaMethod(**parametrs_class_object)
    # table_func = method.solve(**parametrs_for_solver)
    # test_data = test['one_order']['result_last_depend']['rkm']
    # print("one order")
    # print(f'{table_func.table.tail(1)}  ==  {test_data}')
    # # test two_order
    # parametrs_class_object = test['two_order']['parametrs_class_object']
    # parametrs_for_solver = test['two_order']['parametrs_for_solve']
    # #   test
    # method = RungeKuttaMethod(**parametrs_class_object)
    # table_func = method.solve(**parametrs_for_solver)
    # test_data = test['two_order']['result_last_depend']['rkm']
    # print("two order")
    # print(f'{table_func.table.tail(1)}  ==  {test_data}')
