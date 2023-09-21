n = int(input("Введите n: "))

for i in range(1, n + 1):
    for _ in range(i):
        print('+' , end='')
    else:
        print()
