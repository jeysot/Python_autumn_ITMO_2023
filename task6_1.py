a = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9,
     "XC": 90, "XL": 40, "CD": 400, "CM": 900, }


def conv(x):
    count = 0
    while len(x) > 0:
        if x[:2] in a:
            b = x[:2]
            count += a[b]
            x = x[2:]
        else:
            b = x[0]
            count += a[b]
            x = x[1:]

    return count


x = str(input())
print(conv(x))
