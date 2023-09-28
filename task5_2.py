n = int(input())
arr1 = []
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        arr1.append(i)
        arr1.append(n // i)
        arr1.sort()

print(*arr1)

k = 2
while k <= n:
    if n % k == 0:
        count = 0
        while n % k == 0:
            count += 1
            n //= k
        print(f"{k}-{count}")
    k += 1
