def count_skb(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return not stack


print(count_skb("()"))
print(count_skb(")(((()))"))
print(count_skb("("))
print(count_skb("(()) (( () () ) () )"))
print(count_skb("(()"))
