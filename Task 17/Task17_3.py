class Shape:
    def __init__(self, color, square):
        self.color = color
        self.shape = square

    def set_color(self):
        self.color = str(input('Введите цвет: '))

    def info_color(self):
        print(self.color)

    def set_square(self):
        self.square = int(input('Введите площадь: '))

    def info_sqyare(self):
        print(self.square)


cir = Shape("None", 0)

cir.set_color()
cir.info_color()
cir.set_square()
cir.info_sqyare()