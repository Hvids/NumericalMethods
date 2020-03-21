from function_approximation import FunctionApproximation
import sympy
import json

input_file_name = "lab3.4_input.json"

with open(input_file_name,'r') as file:
    data = json.load(file)
    x_vec = data['x']
    f_vec = data['f']
    x_ = data["x_"]

result = {}
fa = FunctionApproximation(1)
fa.make(f_vec,x_vec)
result['df_aprox1'] = fa.diff(x_,1)
fa = FunctionApproximation(2)
fa.make(f_vec,x_vec)
result['df_aprox2'] = fa.diff(x_,1)
result['ddf_aprox2'] = fa.diff(x_,2)
print(f"X = {x_vec}")
print(f'Y = {f_vec}')
print(f'Первая производная первого приблежения')
print(result['df_aprox1'])
print(f'Первая производная второго приблежения')
print(result['df_aprox2'])
print(f'Вторая производная второго приблежения')
print(result['ddf_aprox2'])

output_file_name = "result.json"

with open(output_file_name,'w') as file:
    json.dump(result,file)