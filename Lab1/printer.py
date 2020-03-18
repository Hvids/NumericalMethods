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
        print(f'\t{value}')

def print_eigvals(eigvals):
    for i,eigval in enumerate(eigvals):
        print(f'eigen_{i+1} = {eigval}',end='; ')
    print('')

def print_eigvectors(eigvectors):
    for i,eigvec in enumerate(eigvectors):
        print(f'x{i+1}:')
        print_vector(eigvec)