def count_elements(lst):
    count = 0

    for item in lst:
        count += 1
        if isinstance(item, list):
            count += count_elements(item)

    return count

example1 = [1, 1, [1, 1,[[[1]]]]]
example2 = [1, 2, 3]
example3 = ["x", "y", ["z"]]
example4 = [1, 2, [3, 4, [5]]]

print(count_elements(example1))
print(count_elements(example2))
print(count_elements(example3))
print(count_elements(example4))
