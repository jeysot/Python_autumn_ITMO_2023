import re

def find_car_numbers(text):
    pattern = r'(([А-ЯA-Z]{1}\d{3}[А-ЯA-Z]{2})(78|178))'
    car_numbers = re.findall(pattern, text)
    return car_numbers

# Пример использования функции
text = "Номера автомобилей: A123BC78, X666XX17, L999MM178"
car_numbers = find_car_numbers(text)

print("Найденные номера автомобилей:")
for number, _, region in car_numbers:
    print(number)
