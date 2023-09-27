n = input()
a = {}
for i in str(n):
    if i not in a:
        a[i] = 0
    a[i] += 1

for i in a:
    print(i, a[i])