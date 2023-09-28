import math

def pascal(s):
    ml = []
    for i in range(0, s + 1):
        ml.append(str((math.factorial(s)) // ((math.factorial(i)) * (math.factorial(s - i)))))
    return ml

s = int(input())

for i in range(0, s):
    p = pascal(i)
    p = ' '.join(p)
    print(p)
