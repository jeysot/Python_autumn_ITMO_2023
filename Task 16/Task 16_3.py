
def low(func):
    def wrapper():
        result = func()
        res = result.lower()
        return res
    return wrapper


def say(text):
    print(text.lower())


text = input('Напишите что-то сюда: ')
say = low(say(text))