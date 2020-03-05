class Printer:

    @staticmethod
    def print_matrix(matrix):
        for rows in matrix:
            for value in rows:
                print(value,end=' ')
            print(end='\n')

    @staticmethod
    def print_roots(roots):
        for i, root  in  enumerate(roots):
            print(f'x_{i} = {root}')

    @staticmethod
    def print_vector(vector):
        for value in vector:
            print(value)