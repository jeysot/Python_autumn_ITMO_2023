s = input().split()
a = int(s[0])
b = int(s[-1])
c = s[1]
operations = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}

if c in operations:
    print(operations[c])
else:
    print('error')
