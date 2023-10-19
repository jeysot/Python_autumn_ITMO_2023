first = input()
first = set(tuple(first.split(", ")))
second = input()
second = set(tuple(second.split(", ")))

l = len(first & second)
print(l)


