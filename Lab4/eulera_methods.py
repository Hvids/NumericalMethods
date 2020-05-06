import sympy
import numpy as np
from copy import deepcopy
import pandas as pd


class Method:
    def __init__(self,step,section):
        self.step = step
        self.section = tuple(section)
    @staticmethod
    def precision(real_func,table_func):
        """
        Точность входные данные реальное решение и таличная функиция -> TableFunction
        """
        eps = []
        var = table_func.varibals
        x = table_func.list_value_varibals
        y = table_func.list_value_function
        for yi, xi in zip(y,x):
            yi = yi[0]
            eps.append(abs(real_func.subs(dict(zip(var,xi))) - yi))
        return eps
    @staticmethod
    def precision_runberg(real_func, tablh, tablkh, k, p):
        X1 = np.around(tablh.list_value_varibals.T[0], 5)
        X2 = np.around(tablkh.list_value_varibals.T[0], 5)
        Y1 = tablh.list_value_function.T[0]
        Y2 = tablkh.list_value_function.T[0]
        Y1 = np.array( [yi for xi,yi in zip(X1,Y1) if xi in X2 ])
        Y2 = np.array( [yi for xi,yi in zip(X2,Y2) if xi in X1 ])
        X1 = np.array( [xi for xi in X1 if xi in X2 ])
        F = Y1 + (Y2 - Y1) / (k ** p - 1)


        F_real = np.array([real_func.subs(dict(zip(tablh.varibals, [xi]))) for xi in X1])

        return F, X1,abs(F_real - F)
    
class TableFucntion:
    """
    Табличная функция представление в пандасе
    """
    def __init__(self,table, depend_varibal, varibals):
#         принемает кортеж ключ значния фунции и ключи пременных -> LIST
        self.__table = pd.DataFrame(table)
        self.__depend = depend_varibal
        self.__varibals = varibals
    @property
    def list_value_varibals(self):
#       сисок значений переменной функции
        res = self.__table[self.__varibals].values
        return res
    
    @property
    def list_value_function(self):
#       список значений 
        res = self.__table[self.__depend].values
        return res
    
    
    @property
    def table(self):
        return deepcopy(self.__table)
    
    @property
    def depend_varibale(self):

        return deepcopy(self.__depend)
    
    @property
    def varibals(self):
        return  deepcopy(self.__varibals)
        
            
class ExplicitEuleraMethod(Method):
# Явный метод Эйлера
        
    def solve(self, func_dict,sdata_dict, ans_vars):
#         словарь функции {z': func} начальные данные {x0: val} и конечные пременные выхожа [y,x] 
        h = self.step
        a, b = self.section
        sdata_dict = deepcopy(sdata_dict)
        table_func_dict = { key:[sdata_dict[key]] for key in ans_vars}
        for i in np.arange(a,b,h):
            ndata_dict = deepcopy(sdata_dict)
            for key in sdata_dict.keys():
                if key in func_dict.keys():
                    ndata_dict[key] = sdata_dict[key] + h*func_dict[key].subs(sdata_dict) 
                else:
                    ndata_dict[key] += h
            sdata_dict = deepcopy(ndata_dict)
            for key in ans_vars:
                table_func_dict[key].append(sdata_dict[key])
                
        var_depend = list(set(ans_vars)&set(func_dict.keys()))
        varibals = list(set(ans_vars) - set(var_depend))
        table_func_dict = TableFucntion(table_func_dict,var_depend,varibals)
        return table_func_dict

class EuleraCauchyMethod(Method):
    name = 'Eulera Cauchy Method'
#     Эйлера Коши
    def solve(self, func_dict,sdata_dict, ans_vars):
        h = self.step
        a, b = self.section
        sdata_dict = deepcopy(sdata_dict)
        table_func_dict = { key:[sdata_dict[key]] for key in ans_vars}
        
        for i in np.arange(a,b,h):
            ndata_dict = deepcopy(sdata_dict)
            wave_dict = deepcopy(sdata_dict)
            for key in sdata_dict.keys():
                if key in func_dict.keys():
                    wave_dict[key] = sdata_dict[key] + h*func_dict[key].subs(sdata_dict) 
                else:
                    wave_dict[key] += h
            
            for key in sdata_dict.keys():
                if key in func_dict.keys():
                    ndata_dict[key] = sdata_dict[key] + h*(func_dict[key].subs(sdata_dict) + func_dict[key].subs(wave_dict))/2 
                else:
                    ndata_dict[key] += h
            
            
            sdata_dict = deepcopy(ndata_dict)
            for key in ans_vars:
                table_func_dict[key].append(sdata_dict[key])
        
        var_depend = list(set(ans_vars)&set(func_dict.keys()))
        varibals = list(set(ans_vars) - set(var_depend))
        table_func_dict = TableFucntion(table_func_dict,var_depend,varibals)
        return table_func_dict

class ImprovedEuleraMethod(Method):

    name = 'Improved Eulera Method'
    def solve(self, func_dict,sdata_dict, ans_vars):
        h = self.step
        a, b = self.section
        sdata_dict = deepcopy(sdata_dict)
        table_func_dict = { key:[sdata_dict[key]] for key in ans_vars}

        for i in np.arange(a,b,h):
            ndata_dict = deepcopy(sdata_dict)
            wave_dict = deepcopy(sdata_dict)
            for key in sdata_dict.keys():
                if key in func_dict.keys():
                    wave_dict[key] = sdata_dict[key] + h*func_dict[key].subs(sdata_dict)/2
                else:
                    wave_dict[key] += h/2

            for key in sdata_dict.keys():
                if key in func_dict.keys():
                    ndata_dict[key] = sdata_dict[key] + h*(func_dict[key].subs(wave_dict))
                else:
                    ndata_dict[key] += h


            sdata_dict = deepcopy(ndata_dict)
            for key in ans_vars:
                table_func_dict[key].append(sdata_dict[key])

        var_depend = list(set(ans_vars)&set(func_dict.keys()))
        varibals = list(set(ans_vars) - set(var_depend))
        table_func_dict = TableFucntion(table_func_dict,var_depend,varibals)
        return table_func_dict

if __name__ == "__main__":
    from test_data_lab4_1 import test
#     test one_order
    parametrs_class_object = test['one_order']['parametrs_class_object']
    parametrs_for_solver = test['one_order']['parametrs_for_solve']
#   test eem
    method = ExplicitEuleraMethod(**parametrs_class_object)
    table_func = method.solve(**parametrs_for_solver)
    test_data = test['one_order']['result_last_depend']['eem']
    print('eem')
    print(f'{table_func.table.tail(1)}  ==  {test_data}')

# test ecm
    print('ecm')
    method = EuleraCauchyMethod(**parametrs_class_object)
    table_func = method.solve(**parametrs_for_solver)
    test_data = test['one_order']['result_last_depend']['ecm']
    print(f'{table_func.table.tail(1)}  ==  {test_data}')
# iem
    print('iem')
    method = ImprovedEuleraMethod(**parametrs_class_object)
    table_func = method.solve(**parametrs_for_solver)
    test_data = test['one_order']['result_last_depend']['iem']
    print(f'{table_func.table.tail(1)}  ==  {test_data}')
    # asdasd
    parametrs_class_object['step'] = 0.1
    methdod = ImprovedEuleraMethod(**parametrs_class_object )
    table_fun1 = methdod.solve(**parametrs_for_solver)
    parametrs_class_object ['step'] = 0.05
    methdod = ImprovedEuleraMethod(**parametrs_class_object )
    table_fun2 = methdod.solve(**parametrs_for_solver)

    x, y, z = sympy.symbols('x,y,z')
    real_func = 1 / sympy.cos(x) + sympy.sin(x) + x / sympy.cos(x)
    ImprovedEuleraMethod.precision_runberg(real_func, table_fun1,table_fun2,0.5,2)