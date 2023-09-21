import random

arr1 = []
for i in range(1, random.randint(1, 101)):
    arr1.append(i * random.randint(1,101))

N = len(arr1)
i = 0
while i < N - 1:
    j = 0
    while j < N - 1 - i:
        if arr1[j] > arr1[j+1]:
            arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
        j += 1
    i += 1

print(arr1[0])
