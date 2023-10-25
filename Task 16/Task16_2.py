import re

def find_numbers(num, arr):
    pattern = r'\b(?:[0-9]|[1-{}][0-9])\b(?![0-9])'.format(num, num)
    matches = re.findall(pattern, ' '.join(map(str, arr)))
    return list(map(int, matches))


num = int(input('Введите положительное целое число: '))
arr1 = [0, 1, 5, 10, 15, 99, 20, 25, 30, 45, 60, 1, 70, 80, 100]
result = find_numbers(num, arr1)
result = [x for x in result]
print(' '.join(map(str, result)))