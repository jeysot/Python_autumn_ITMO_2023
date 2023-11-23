from functools import cmp_to_key

def largest_number(nums):
    def compare(x, y):
        return int(x + y) - int(y + x)

    sorted_nums = sorted(map(str, nums), key=cmp_to_key(compare), reverse=True)

    result = ''.join(sorted_nums)

    return result

input1 = [32,3,45]
result1 = largest_number(input1)
print(f"Для входа {input1}, результат: {result1}")

