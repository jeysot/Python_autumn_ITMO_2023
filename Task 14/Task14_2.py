def sum_num(n):
    if n < 10:
        return n
    else:
        return sum_num(n // 10) + n % 10


print(sum_num(int(input('Введите число: '))))
