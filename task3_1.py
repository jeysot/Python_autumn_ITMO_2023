zp = []
while True:
    n = int(input())
    if n == 0:
        break
    zp.append(n)

print(sum(zp)//len(zp))