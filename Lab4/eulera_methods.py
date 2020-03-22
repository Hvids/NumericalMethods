import sympy
import numpy as np
from copy import deepcopy
import pandas as pd

class Method:
    def __init__(self,step,section):
        self.step = step
        self.section = tuple(section)
        
    def precision(self,real_func,table_func):
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
        return self.__table
    
    @property
    def depend_varibale(self):
        return self.__depend
    
    @property
    def varibals(self):
        return self.__varibals
        
            
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