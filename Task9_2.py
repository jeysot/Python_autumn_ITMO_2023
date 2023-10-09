vowel = ['а', 'у', 'о', 'ы', 'и', 'э', 'ю', 'я', 'ё', 'е', 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Ю', 'Я', 'Ё', 'Е']
arr = []

def similar(x, n, arr):
    vowel_positions = [i for i, char in enumerate(x) if char in vowel]
    matching_words = []
    for word in arr:
        vowel_positions_word = [i for i, char in enumerate(word) if char in vowel]
        if vowel_positions == vowel_positions_word:
            matching_words.append(word)
    return matching_words


x = str(input('Введите слово для сравнения: '))
n = int(input('Сколько будет слов для проверки: '))
for i in range(n):
    word = input('Введите слово: ')
    arr.append(word)

print(*similar(x, n, arr))