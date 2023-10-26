# def sample_decorator(func):
#     def wraepper():
#         print("Start")
#         func()
#         print('Finish')
#     return wraepper
#
# def say():
#     print("Hi")
# say = sample_decorator(say)
# say()
#
# @sample_decorator
# def bye():
#     print('Bye')
# # bye()
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         value = func(*args, **kwargs)
#         return value
#     return wrapper

# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         val = func(*args,**kwargs)
#         end = time.perf_counter()
#         work_time = end - start
#         print(f'Время выполнения {func.__name__}:{round(work_time, 4)} сек')
#         return val
#     return wrapper
#
# @timer
# def test(n):
#     return sum([(i/99)**2 for i in range(n)])
#
# @timer
# def sleep(n):
#     time.sleep(n)
#
# res1 = test(10000)
# res2 = sleep(4)
# print(f'Результат функции test = {res1}')
# print(f'Результат функции sleep = {res2}')
# import time
#
#
# def clue(func):
#     def wrapper(*args, **kwargs):
#         with open('log.txt', 'w') as f:
#             print(time.time(), 'start', {func.__name__}, file = f)
#         func(*args, **kwargs)
#         with open('log.txt', 'w') as f:
#             print(time.time(), 'start', {func.__name__}, file = f)
#         res = ''
#         for i in args:
#             res += i
#         return res
#     return wrapper
#
# @clue
# def test(*args):
#     return None
#
# print(test('haha', 'baba', 'caca'))
#
# @clue
# def comp_str(x, y):
#     return x > y
# print(comp_str('a', 'b'))


# class Person:
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#
#     def give_money(self, other, x_money):
#         if other.money < x_money:
#             print('Не хватает денег!')
#         else:
#             other.money += x_money
#             self.money -= x_money
#     def soc(self, other):
#         if self.money != other.money:
#             dif = abs(self.money - other.money) // 2
#             if self.money < other.money:
#                 self.money += dif
#                 other.money -= dif
#             else:
#                 self.money -= dif
#                 other.money += dif
#
#     def info(self):
#         print(self.name, self.money)
#
#
#
# a = Person('Pete', 200)
# b = Person('Nick', 300)
# a.give_money(b, 500)
# b.give_money(a, 200)
# print(a.money, b.money)
# a.info()
# b.info()
# a.soc(b)
# a.info()
# b.info()



