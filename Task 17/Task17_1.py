import re

def twins(s):
    pattern = r'\b(\w+)(?:\s+\1\b)+'
    new = re.sub(pattern, r'\1', s)
    return new

s = "Напишите программу программу, которая устраняет повторение " \
    "повторение слов, т.е. результат результат должен быть таким."


print(twins(s))