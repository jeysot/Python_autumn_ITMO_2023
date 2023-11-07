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


# class Figure:
#     def __init__(self, color, peri=0):
#         self.peri = peri
#         self.color = color
#
#     def get_peri(self, peri):
#         print(self.peri)
#         return
#
# a = Figure('Red', 100)
# b = Figure('Blue')


# class Student:
#     def __init__(self, name):
#         print('Inside constructor')
#         self.name = name
#         print('Object initialized')
#
#     def show(self):
#         print('Hello, my name is', self.name)
#
#
# def __del__(self):
#     print('Inside destructor')
#     print('Object destroyed')
#
#
# s1 = Student('Emma')
# s1.show()
# del s1
# s1.show()


# class Student:
#     lst = []
#     def __init__(self, name):
#         self.name = name
#         Student.lst.append(self.name)
#
#     def info(self):
#         print(f'Name: {self.name}')
#         print(Student.lst)
#
# s1 = Student('Emma')
# s1.info()
# s2 = Student('Bob')
# s2.info()
#
# class Tree(object):
#     def __init__(self, kind, height):
#         self.kind = kind
#         self.age = 0
#         self.height = height
#
#     def grow(self):
#         self.age += 1
#
#
# class FruitTree(Tree):
#     def __init__(self, kind, height):
#         super().__init__(kind, height)
#
#     def give_fruits(self, how_many):
#         print(f"{how_many} of {self.kind}")
#
# # f_tree = FruitTree('apple', 0.7)
# # f_tree.give_fruits()
# # f_tree.grow()
#
# b = FruitTree('orange', 0.5)
# b.give_fruits(2)

#
# class Figure:
#     def __init__(self, color, peri=0):
#         self.color = color
#         self.peri = peri
#
#
# class Triangle(Figure):
#     def __init__(self, color, a, b, c):
#         self.color = color
#         self.a = a
#         self.b = b
#         self.c = c
#     def set_peri(self):
#         self.peri = self.a + self.b + self.c
#
# class  rectangle(Figure):
#     def __init__(self,color,  le, wi):
#
#
#
# abc = Triangle('Red', 3, 4, 5)
# abc.set_peri()
# print(abc.peri)
# print(abc.color)

#
# class Student:
#     stdnt = []
#
#     def __init__(self, name, fives, tens, twenties):
#         self.name = name
#         self.fives = fives
#         self.tens = tens
#         self.twenties = twenties
#         Student.stdnt.append(self)
#
#     def result(self):
#         for st in Student.stdnt:
#             su = st.fives * 5 + st.tens * 10 + st.twenties * 20
#             print(st.name, su)
#
#
# a = Student('Ivan', 1, 17, 19)
# b = Student('Petr', 29, 12, 2)
# c = Student('Cead', 0, 0, 1)
# a.result()


# class SC():
#     def __init__(self):
#         self.__param = 42
#
# obj = SC()
# # obj.__param
# print(obj._SC__param)

import random

class Teacher:
    def __init__(self, name):
        self.name = name

    def assign_task(self, pupil, task):
        pupil.receive_task(task)

    def check_task(self, pupil, task, task_description):
        marks_obj = Marks()
        mark = marks_obj.get_mark()
        pupil.receive_feedback(mark, task_description)


class Pupil:
    def __init__(self, name):
        self.name = name
        self.task = None
        self.mark = None

    def receive_task(self, task):
        self.task = task

    def is_solve_task(self):
        if self.task:
            self.task.solve_task()

    def receive_feedback(self, mark, task_description):
        self.mark = mark
        print(f"{self.name} получил оценку {self.mark} по {task_description}")


class Marks:
    def __init__(self):
        self.mark = self.get_mark()

    def get_mark(self):
        marks = {2: "плохо", 3: "удовлетворительно", 4: "хорошо", 5: "отлично"}
        self.mark = marks[random.choice(range(2, 6))]
        return self.mark


class Task:
    def __init__(self, task_description):
        self.task_description = task_description
        self.status = None
        marks_obj = Marks()
        self.mark = marks_obj.mark

    def solve_task(self):
        if self.mark != 'Плохо':
            self.status = "Решенная"
        else:
            self.status = "Нерешенная"


teacher = Teacher("Преподаватель")
pupil1 = Pupil("Ученик 1")
pupil2 = Pupil("Ученик 2")
pupil3 = Pupil("Ученик 3")

task_description1 = "задаче 1"
task1 = Task(task_description1)
task_description2 = "задаче 2"
task2 = Task(task_description2)

teacher.assign_task(pupil1, task1)
teacher.assign_task(pupil1, task2)
teacher.assign_task(pupil2, task1)
teacher.assign_task(pupil2, task2)
teacher.assign_task(pupil3, task1)
teacher.assign_task(pupil3, task2)

pupil1.receive_task(task1)
pupil1.receive_task(task2)
pupil2.receive_task(task1)
pupil2.receive_task(task2)
pupil3.receive_task(task1)
pupil3.receive_task(task2)

pupil1.is_solve_task()
pupil2.is_solve_task()
pupil3.is_solve_task()

teacher.check_task(pupil1, task1, task_description1)
teacher.check_task(pupil1, task2, task_description2)
teacher.check_task(pupil2, task1, task_description1)
teacher.check_task(pupil2, task2, task_description2)
teacher.check_task(pupil3, task1, task_description1)
teacher.check_task(pupil3, task2, task_description2)