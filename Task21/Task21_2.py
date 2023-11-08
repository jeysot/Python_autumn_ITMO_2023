def find_minimal_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    min_sum_matrix = [[0] * cols for _ in range(rows)]
    min_sum_matrix[0][0] = matrix[0][0]

    for j in range(1, cols):
        min_sum_matrix[0][j] = min_sum_matrix[0][j - 1] + matrix[0][j]

    for i in range(1, rows):
        min_sum_matrix[i][0] = min_sum_matrix[i - 1][0] + matrix[i][0]

    for i in range(1, rows):
        for j in range(1, cols):
            min_sum_matrix[i][j] = matrix[i][j] + min(min_sum_matrix[i - 1][j], min_sum_matrix[i][j - 1])

    return min_sum_matrix[rows - 1][cols - 1]


matrix = [[10, 20, 30], [5, 1, 80], [90, 2, 70]]
minimal_sum = find_minimal_sum(matrix)
print("Минимальная сумма:", minimal_sum)
