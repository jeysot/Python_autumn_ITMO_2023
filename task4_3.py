def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

word1 = input("Введите первое предложение: ")
word2 = input("Введите второе предложение: ")

if is_anagram(word1, word2):
    print(True)
else:
    print(False)