def genetics(arr1):
    i = 0
    while i < len(arr1) - 1:
        tek = arr1[i]
        sled = arr1[i+1]
        if (tek == "А" and sled == "Г") or (tek == "Г" and sled == "А"):
            arr1[i] = sled
            arr1[i+1] = tek
            i = i + 1
        if (tek == "Ц" and sled == "Т") or (tek == "Т" and sled == "Ц"):
            arr1.insert(i+1, "А")
            arr1.insert(i+2, "Г")
            i = i + 2
        i = i + 1
    return arr1

string = input("Введите строку кода заглавными русскими буквами: ")
arr1 = list(string)
print(''.join(genetics(arr1)))