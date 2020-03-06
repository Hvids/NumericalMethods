def print_matrix(matrix):
    for rows in matrix:
        for value in rows:
            print(value,end=' ')
        print(end='\n')


def print_roots(roots):
    for i, root  in  enumerate(roots):
        print(f'x_{i} = {root}')


def print_vector(vector):
    for value in vector:
        print(value)