from cubic_splatsn import CubicSplatsn
import  sympy
import json
input_file_name = "lab3.2_input.json"

with open(input_file_name,'r') as file:
    data = json.load(file)
    x_vec = data['x']
    f_vec = data['f']
    x_ = data["x_"]

cup_sp = CubicSplatsn(f_vec,x_vec)
for i,sp in enumerate(cup_sp.cubic_splatsn):
    print(f'f{i} = ')
    sympy.pprint(sp)

f_x_ = cup_sp.calc_point(x_)
print(f'\n\nf({x_}) = {f_x_}')

output_file_name = "result.json"

with open(output_file_name,'w') as file:
    file.write(f'(f{x_}) = {f_x_}')