n = int(input())

matrix = [[0] * n for _ in range(n)]

# Определяем границы
top = 0
bottom = n - 1
left = 0
right = n - 1

# Заполняем матрицу по спирали
num = 1
while num <= n * n:
    # Заполняем верхнюю границу слева направо
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1

    # Заполняем правую границу сверху вниз
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    # Заполняем нижнюю границу справа налево
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1

    # Заполняем левую границу снизу вверх
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

# Выводим матрицу
for row in matrix:
    for num in row:
        print(str(num).ljust(3), end='')
    print()