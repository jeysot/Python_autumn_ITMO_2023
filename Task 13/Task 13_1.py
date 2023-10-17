def gen():
    num = 1
    while True:
        yield num
        num += 1
        yield -num
        num += 1
g = gen()
for _ in range(10):
    print(next(g))
