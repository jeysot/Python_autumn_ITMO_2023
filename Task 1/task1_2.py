arr1 = []


x = int(input('Введите x: '))
y = int(input('Введите y: '))


arr1.append(x + y)
arr1.append(x - y)
arr1.append(x * y)
arr1.append(x / y)
arr1.append(x // y)


print(max(arr1))
