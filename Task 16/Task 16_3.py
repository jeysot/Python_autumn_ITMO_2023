
def low(func):
    def wrapper():
        func()
    return wrapper


def say(text):
    print(text.lower())


text = input('Напишите что-то сюда: ')
say = low(say(text))