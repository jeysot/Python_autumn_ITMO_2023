def max3(x):
    flattened = [num for sublist in x for num in sublist] # Преобразуем двумерный список в одномерный
    sorted_nums = sorted(set(flattened), reverse=True) # Сортируем числа
    return sorted_nums[:3] # Возвращаем первые три самых больших числа

n = int(input())
m = int(input())
x  = []
for i in range(n):
    for j in range(m):
        x.append(input())

result = max3(x)
print(*result[::-1])