def decorator(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return value

    return wrapper


@decorator
def up(*args, **kwargs):
    res = []
    for x in args:
        if isinstance(x, str):
            res.append(x.upper())
    for x in kwargs.values():
        if isinstance(x, str):
            res.append(x.upper())
    print(res)


result = up('hi', 54, 'python', **{'1': 'Red', '2': "Blue", '3': 4})
