import re

def func(text):
    words = re.findall(r'\b\w', text)
    result = ''.join(words).upper()
    return result


sentence = input(str('Введите строку: '))

acronym = func(sentence)
print(acronym)
