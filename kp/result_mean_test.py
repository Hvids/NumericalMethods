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





PATH_IN  = './global_test/'
PATH_OUT = './'

times_mean_simple_out_name = 'mean_simple'
times_mean_omp_out_name = 'mean_omp'

times_simple_names = [PATH_IN + f'test_simple_{i}' for i in range(0,9)]
times_omp_names = [PATH_IN + f'test_omp_{i}' for i in range(0,9)]

times_omps = []
times_simples  = []

for to_name,ts_name in zip(times_omp_names, times_simple_names):
    to = read_time(to_name)
    ts = read_time(ts_name)
    times_omps.append(to)
    times_simples.append(ts)
times_omps = np.array(times_omps).T.mean(1)
times_simples = np.array(times_simples).T.mean(1)

write_time(times_omps, PATH_OUT+times_mean_omp_out_name)
write_time(times_simples,PATH_OUT+times_mean_simple_out_name)
