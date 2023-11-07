# class Task:
#     def __init__(self):
#         self.index = 1
#         self.letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index > 26:
#             self.index = 1
#         current_index = self.index
#         self.index += 1
#         if current_index % 26 == 0:
#             letter = self.letters[-1]
#         else:
#             letter = self.letters[current_index % 26 - 1]
#         return current_index, letter
#
#
# s = Task()
#
#
# for _ in range(30):
#     print(*next(s), end=',')
class CyclicSequenceGenerator:
    def __init__(self):
        self.current_number = 1
        self.current_letter = 'A'

    def __iter__(self):
        return self

    def __next__(self):
        element = f"{self.current_number}, {self.current_letter}"

        # Обновляем текущее число и букву
        if self.current_number == 26:
            self.current_number = 1
            if self.current_letter == 'Z':
                self.current_letter = 'A'
            else:
                self.current_letter = chr(ord(self.current_letter) + 1)
        else:
            self.current_number += 1
            self.current_letter = chr(ord(self.current_letter) + 1)

        return element

# Пример использования:
generator = CyclicSequenceGenerator()
for _ in range(50):
    print(next(generator), end=', ')

