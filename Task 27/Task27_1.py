def generate_darts_matrix(n):
    if not (1 <= n <= 18):
        print("Введите число n от 1 до 18.")
        return

    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n - i):
            matrix[i][j] = matrix[j][i] = matrix[n - i - 1][j] = matrix[j][n - i - 1] = min(i, j) + 1

    for row in matrix:
        print(" ".join(map(str, row)))


n = int(input("Введите число n от 1 до 18: "))
generate_darts_matrix(n)
