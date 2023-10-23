import re

def find_phone_numbers(text):
    pattern = r'(\+7\((812|921)\)\d{3}-\d{2}-\d{2}|\+7\((812|921)\)\d{3}-\d{4})'
    phone_numbers = re.findall(pattern, text)
    correct = []
    for num in phone_numbers:
        correct.append(num[0])
    return correct

# Пример использования функции
text = "+7(812)123-45-67, +7(921)987-65-43, +7(812)111-2233, +7(911)555-6677"
phone_numbers = find_phone_numbers(text)
for numb in phone_numbers:
    print(numb)
