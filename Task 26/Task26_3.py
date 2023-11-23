class Person:
    def __init__(self):
        self._age = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 1 <= value <= 100:
            self._age = value
        else:
            print("Недопустимый возраст")

    @age.deleter
    def age(self):
        print("Удаление возраста")
        del self._age


person = Person()


person.age = 25
print(person.age)

person.age = 120


del person.age 
