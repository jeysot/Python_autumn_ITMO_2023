num = input("Введите последовательность чисел через пробел: ").split()
count = 0

for number in num:
    if int(number) == 10:
        count += 1

print("Количество чисел равных 10: ", count)

