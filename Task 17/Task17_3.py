class Shape:
    def __init__(self, color, square):
        self.color = color
        self.square = square

    def set_color(self):
        self.color = str(input('Введите цвет: '))

    def get_color(self):
        print(self.color)

    def set_square(self):
        self.square = int(input('Введите площадь: '))

    def get_square(self):
        print(self.square)


cir = Shape("None", 0)

cir.set_color()
cir.get_color()
cir.set_square()
cir.get_square()