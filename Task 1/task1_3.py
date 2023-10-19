arr1 = []

x = int(input('Введите x: '))
y = int(input('Введите y: '))

arr1.append(int(x + y))
arr1.append(int(x - y))
arr1.append(int(x * y))
arr1.append(int(x / y))
arr1.append(int(x // y))

arr1 = sorted(arr1)

print(arr1[-2])

