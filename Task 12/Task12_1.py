def minimum(lst):
    min_x = min(lst)
    max_x = max(lst)

    min_ind = [i for i, x in enumerate(lst) if x == min_x]
    max_ind = [i for i, x in enumerate(lst) if x == max_x]

    return min_ind, max_ind

x = [1, 2, 3, 4, 1, 2, 3, 4, 1, 4]
min_ind, max_ind = minimum(x)
print(min_ind, max_ind)
