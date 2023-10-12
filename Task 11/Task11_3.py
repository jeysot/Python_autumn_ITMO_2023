def arabic_to_roman(number):
    if not 1 <= number <= 3999:
        return "Неверное число"

    num = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }

    roman_number = ''
    for value in sorted(num.keys(), reverse=True):
        while number >= value:
            roman_number += num[value]
            number -= value
    return roman_number


arabic_number = int(input())
roman_number = arabic_to_roman(arabic_number)
print(f"Арабское число {arabic_number} в римской нотации: {roman_number}")
