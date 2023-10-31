import itertools

money = [50, 100, 200, 500, 1000, 5000]

all_money = []
for i in range(1, len(money) + 1):
    combs = itertools.combinations(money, i)
    for comb in combs:
        summ = sum(comb)
        all_money.append(summ)


all_money = list(set(all_money))
all_money.sort()

print(all_money)
