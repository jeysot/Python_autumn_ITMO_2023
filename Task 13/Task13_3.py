def odd_numbers(input_list):
    for num in input_list:
        if num % 2 != 0:
            yield num

input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
g = odd_numbers(input_numbers)

for num in g:
    print(num)
