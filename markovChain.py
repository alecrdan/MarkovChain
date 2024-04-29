import csv
from fractions import Fraction


def csv_to_matrix(csv_file):
    matrix = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            row = [Fraction(cell) if '/' in cell else Fraction(float(cell)
                                                               ).limit_denominator() if cell else 0 for cell in row]
            matrix.append(row)
    return matrix


def print_first_column(matrix):
    for row in matrix:
        print(row[0])


def print_all_columns(matrix):
    num_columns = len(matrix[0])
    for col_index in range(num_columns):
        for row in matrix:
            print(row[col_index])


def markovChain(matrix, x0, num_steps):
    chain = []
    x = x0
    for step in range(num_steps):
        x_new = [0] * len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                x_new[i] += matrix[i][j] * x[j]
        chain.append(x_new)
        x = x_new
    return chain


def fractions_to_decimals(chain):
    for step, x_new in enumerate(chain):
        decimals = [float(x) for x in x_new]
        print("\nStep {}: {}".format(step, decimals))


# Usage
csv_file = 'matrix2.csv'
matrix = csv_to_matrix(csv_file)
x0 = [1] + [0] * (len(matrix) - 1)  # Vector
num_steps = 20  # Number of steps
chain = markovChain(matrix, x0, num_steps)
fractions_to_decimals(chain)
