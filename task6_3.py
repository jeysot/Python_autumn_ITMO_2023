def symbol(s):
    numb = []
    let = []
    oth = []
    for i in s:
        if i.isdigit() == True:
            numb.append(i)
        elif i.isalpha() == True:
            let.append(i)
        else:
            oth.append(i)
    return numb, let, oth


s = str(input())
pr = symbol(s)
for i in pr:
    print(*sorted(set(i)))
