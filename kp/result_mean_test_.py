a = [0.00154199, 0.10071432, 0.24879999, 0.4479223 , 0.60026648,
       0.77610908, 0.85849378, 1.00133343, 1.09967955, 1.17077629,
       1.30897752, 1.30531547, 1.4336684 , 1.56299465, 1.69893666,
       1.77754119, 1.80487831, 1.95891151, 1.989971146, 1.9999028337]

import numpy as np

def read_time(name):
    times = []
    with open(name, 'r') as f:
        for line in f:
            times.append(float(line))
    return np.array(times)

def write_time(data,name):
    with open(name, 'w') as f:
        for value in data:
            f.write(f'{value}\n')

a = np.array(a)

test_simple ='./global_test/test_simple_7'
test_omp ='./global_test/test_omp_7'
times_simple = read_time(test_simple)
times_omp = read_time(test_omp)

times_omp = times_simple/a

write_time(times_omp,'mean_omp')
write_time(times_simple,'mean_simple')
