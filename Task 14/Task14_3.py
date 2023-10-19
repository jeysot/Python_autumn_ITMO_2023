def tri_2(n):
    if n == 1:
        return print('*')
    print('*' * n)
    tri_2(n - 1)
    print('*' * n)


n = int(input('n: '))
print(tri_2(n))