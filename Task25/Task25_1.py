# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
# Постой вариант
# class CounterApp(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.init_ui()
#
#     def init_ui(self):
#         self.counter = 0
#
#         self.label = QLabel('Нажатий: 0', self)
#
#         self.button = QPushButton('Нажми меня', self)
#         self.button.clicked.connect(self.on_button_click)
#
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.label)
#         layout.addWidget(self.button)
#
#         self.setWindowTitle('Счетчик нажатий')
#         self.show()
#
#     def on_button_click(self):
#         self.counter += 1
#         self.label.setText(f'Нажатий: {self.counter}')
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = CounterApp()
#     sys.exit(app.exec())


# СЛОЖНЫЙ ВАРИАНТ
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.num1_edit = QLineEdit(self)
        self.num2_edit = QLineEdit(self)
        self.result_label = QLabel('Результат: ', self)

        self.add_button = QPushButton('+', self)
        self.subtract_button = QPushButton('-', self)
        self.multiply_button = QPushButton('*', self)
        self.divide_button = QPushButton('/', self)

        self.add_button.clicked.connect(self.calculate)
        self.subtract_button.clicked.connect(self.calculate)
        self.multiply_button.clicked.connect(self.calculate)
        self.divide_button.clicked.connect(self.calculate)

        layout = QVBoxLayout(self)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.num1_edit)
        input_layout.addWidget(self.num2_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.subtract_button)
        button_layout.addWidget(self.multiply_button)
        button_layout.addWidget(self.divide_button)

        layout.addLayout(input_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.result_label)

        self.setWindowTitle('Калькулятор')
        self.show()

    def calculate(self):
        num1 = float(self.num1_edit.text())
        num2 = float(self.num2_edit.text())

        sender = self.sender()

        if sender == self.add_button:
            result = num1 + num2
        elif sender == self.subtract_button:
            result = num1 - num2
        elif sender == self.multiply_button:
            result = num1 * num2
        elif sender == self.divide_button:
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Ошибка: деление на ноль'
                self.result_label.setText(f'Результат: {result}')
                return

        self.result_label.setText(f'Результат: {result}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalculatorApp()
    sys.exit(app.exec())
