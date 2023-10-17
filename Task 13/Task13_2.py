def palin(num):
    return str(num) == str(num)[::-1]


def gen():
    num = 1
    while True:
        if palin(num):
            yield num
        num += 1


g = gen()
for _ in range(50):
    print(next(g))
