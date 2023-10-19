def nod(a, b):
    while b:
        a, b = b, a % b
    return a


def nok(a, b):
    # НОК = (a * b) / НОД(a, b)
    return (a * b) // nod(a, b)


def find_lcm(numbers):
    if len(numbers) == 0:
        return
    elif len(numbers) == 1:
        return numbers[0]

    lcm_result = numbers[0]
    for i in range(1, len(numbers)):
        lcm_result = nok(lcm_result, numbers[i])

    return lcm_result


print(find_lcm([3, 6, 9]))
