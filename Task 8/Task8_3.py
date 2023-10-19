lst = ['abab','xx','aaaaaaa','abcbab']
lst2 = sorted(lst, key=lambda x: (-len(set(x)), x))
print(lst2)