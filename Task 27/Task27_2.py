class Item:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name.capitalize()

    @property
    def total(self):
        return self._price * self._quantity


item = Item("book", 10, 2)

print(f"Название предмета: {item.name}")
print(f"Общая стоимость: {item.total} рублей")
