
class Task:
    def __init__(self):
        self.current_number = 1
        self.current_letter = 'A'

    def __iter__(self):
        return self

    def __next__(self):
        element = f"{self.current_number}, {self.current_letter}"

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

s = Task()
for _ in range(50):
    print(next(s), end=', ')

