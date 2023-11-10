import keyword
kwlist = keyword.kwlist

s = "hello i'm from russia and i love cats and it's True that i'm not man or dog".split()
for i in range(len(s)):
    if s[i] in kwlist:
        s[i] = '<kw>'

print(*s)
