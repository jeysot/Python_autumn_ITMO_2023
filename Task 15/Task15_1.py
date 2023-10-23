def get_values(dct, x):
    values = []
    for key, value in dct.items():
        if key == x:
            values.append(value)
        elif isinstance(value, dict):
            values.extend(get_values(value, x))
    return values


dct = {1: 1, 2: 2, 3: {2: 22, 3: {1: 111, 2: 222, 3: {0: 1111, 1: 2222, 2: 3333}}, 1: 11, }, 6: 22}
x = int(input('Введите ключ к dct: '))

result = get_values(dct, x)
print(result)
