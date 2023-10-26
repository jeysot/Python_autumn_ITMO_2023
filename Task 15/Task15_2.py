import re
def print_car_numbers(text):
    text = text.upper()
    pattern = re.compile(r'[АОМТВНЕРХСУКAOMTBHEPXCYK]{1}[0-9]{3}[АОМТВНЕРХСУКAOMTBHEPXCYK]{2}[178]{3}|[АОМТВНЕРХСУКAOMTBHEPXCYK]{1}[0-9]{3}[АОМТВНЕРХСУКAOMTBHEPXCYK]{2}[78]{2}')
    matches = re.findall(pattern, text)
    for match in matches:
        print(match)
text = input('Введите номера автомобилей через запятую: ')
print_car_numbers(text)