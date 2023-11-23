def bubble_sort(num):
    n = len(num)

    for i in range(n):
        for j in range(0, n - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]

numbers = [64, 34, 25, 12, 22, 11, 90, 5]
bubble_sort(numbers)
print("Отсортированный список:", numbers)
