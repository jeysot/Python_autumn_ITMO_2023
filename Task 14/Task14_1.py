def len_num(n):
    if n < 10:
        return 1
    else:
        return len_num(n // 10) + 1


print(len_num(int(input('Введите число: '))))
