import re


def low(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.lower()
        return result
    return wrapper


@low
def say():
    str = input('Напишите что-то сюда: ')
    return str


print(say())