n = int(input())
arr1 = []

if n == 0:
    print('1')
if n == 1:
    print('1')

else:
    arr1 = [1, 1]
    for i in range(2, n + 1):
        arr1.append(arr1[i - 1] + arr1[i - 2])

if 0 in arr1:
    arr1.remove(0)

print(" ".join(map(str, arr1)))