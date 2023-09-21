n = int(input("Введите n: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        if i % 5 == 0:
            print('FizzBuzz')
            continue
        print('Fizz')
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    elif i % 5 == 0:
        print('Buzz')

