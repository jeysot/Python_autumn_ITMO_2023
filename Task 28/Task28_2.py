function = lambda s1, s2: sum(c1 != c2 for c1, c2 in zip(s1, s2))
print(function("abc", "abc"))
print(function("abc", "abd"))
print(function("abc", "xyz"))

