def tri_2(n):
    if n == 1:
        print('*')
        return
    print('*' * n)
    tri_2(n - 1)
    print('*' * n)
    return


n = int(input('n: '))
tri_2(n)