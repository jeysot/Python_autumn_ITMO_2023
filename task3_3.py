s = input().split()
l = 0
ind = 0
word = []
for i in s:
    if len(i) > l:
        l = len(i)
        ind = s.index(i)

print(''.join(s[ind]))
