def longest_palindrome_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    max_length = 1
    start = 0
    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_length = 2
            start = i

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                max_length = length
                start = i

    return s[start:start + max_length]


s = input("Введите строку: ")
longest_palindrome = longest_palindrome_substring(s)
print("Самая длинная палиндромная подстрока:", longest_palindrome)
