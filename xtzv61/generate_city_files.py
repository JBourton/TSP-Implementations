def generate_upper_triangular_matrix(city_sizes):
    n = len(city_sizes)
    upper_triangular_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            upper_triangular_matrix[i][j] = city_sizes[j - i]
    return upper_triangular_matrix

def write_matrix_to_file(matrix, filename):
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

city_sizes = [
    12, 21, 14, 40, 32, 15, 30, 5, 9, 31, 7, 13,
    13, 8, 8, 4, 7, 35, 14, 17, 12, 11,
    7, 10, 9, 34, 10, 4, 4, 31, 35,
    3, 6, 20, 53, 15, 2, 30, 29,
    3, 25, 32, 16, 5, 40, 21,
    10, 30, 15, 8, 9, 9,
    50, 32, 40, 20, 6,
    6, 30, 12, 20,
    15, 21, 25,
    50, 27,
    5
]

size = 12  # Size of the upper triangular matrix

upper_triangular_matrix = generate_upper_triangular_matrix(city_sizes[:size])
write_matrix_to_file(upper_triangular_matrix, 'city_files/city_12.txt')