class Person:
    def __init__(self, name, payment_method):
        self.name = name
        self.payment_method = payment_method

    def order_coffee(self, cafe, coffee, cake=None):
        order = {'кофе': coffee, 'пирожное': cake}
        cafe.take_order(self, order)

    def pay(self, summ):
        if self.payment_method == "наличные":
            print(f"{self.name} оплатил наличными: {summ} рублей.")
        elif self.payment_method == "карта":
            print(f"{self.name} оплатил картой: {summ} рублей.")
        else:
            print("Неподдерживаемый способ оплаты")
        pass


class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cafe:
    def __init__(self, name):
        self.name = name
        self.order = []

    def take_order(self, client, order):
        self.order.append((client, order))



menu = {"Эспрессо": 100, "Капучино": 150, "Латте": 180, "Пирожное": 50}
cafe = Cafe("Мой Кафе", )

person1 = Person("Анна", "карта")
person2 = Person("Петр", "наличные")

person1.order_coffee(cafe, "Капучино", "Чизкейк")
person2.order_coffee(cafe, "Эспрессо")

person1.pay(150)
person2.pay(100)