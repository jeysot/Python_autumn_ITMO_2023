class Person:
    def __init__(self, last_name, first_name, patronymic):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic

    def __str__(self):
        reversed_last_name = self.last_name[::-1]
        reversed_first_name = self.first_name[::-1]
        reversed_patronymic = self.patronymic[::-1]
        full_name_reversed = f"{reversed_patronymic}{reversed_first_name}{reversed_last_name}"
        return full_name_reversed


p = Person('Иванов', 'Михаил', 'Федорович')
print(p)
me = Person('Сотникова', 'Евгения', 'Олеговна')
print(me)
