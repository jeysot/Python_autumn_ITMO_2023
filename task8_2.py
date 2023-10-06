list = [[1, 5, 3], [2, 44, 1, 4], [3, 3]]

# Функция для вычисления общего количества цифр в подсписке
def count_digits(sublist):
    return sum(map(lambda x: len(str(x)), sublist))

# Сортировка каждого подсписка по убыванию
sorted_sublists = [sorted(sublist, reverse=True) for sublist in input_list]

# Сортировка внешнего списка по возрастанию общего количества цифр в каждом подсписке
sorted_list = sorted(sorted_sublists, key=count_digits)

print(sorted_list)
