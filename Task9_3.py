def count_letter(text):
    text = text.lower()
    dictionary = {}
    for char in text:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    sorted_dict = sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))
    for i in range(min(10, len(sorted_dict))):
        print(sorted_dict[i][0], ":", sorted_dict[i][1])


text = str(input('Введите текст: '))
print()
count_letter(text)