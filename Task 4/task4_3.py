def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


word1 = input("Введите первое предложение: ").lower()
word2 = input("Введите второе предложение: ").lower()

word3 = ''
word4 = ''

alp = 'abcdefghijklmopqrstuvwxyz'
for i in word1:
    if i in alp:
        word3+=i

for i in word2:
    if i in alp:
        word4 += i

if is_anagram(word3, word4):
    print(True)
else:
    print(False)
