def recursive_dict_search(dct, x):
    result = []
    for key, value in dct.items():
        if key == x:
            result.append({key: value})
        elif isinstance(value, dict):
            nested_result = recursive_dict_search(value, x)
            for item in nested_result:
                result.append({key: item})
    return result

# Пример использования функции
dct = {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11,}, 6:22}
x = 1
result = recursive_dict_search(dct, x)
print(result)
