def num(s):
    ranges = s.split(',')
    numbers = []
    for i in ranges:
        start, end = i.split('-')
        start = int(start)
        end = int(end)
        numbers += list(range(start, end + 1))
    return numbers


s = '1-2,4-4,3-6'

print(num(s))
