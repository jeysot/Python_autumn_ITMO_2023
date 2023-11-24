def count_inversions(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count


arr1 = [5, 3, 4, 3, 2]
arr2 = [5, 4, 3, 2, 1]

print(count_inversions(arr1))
print(count_inversions(arr2))
