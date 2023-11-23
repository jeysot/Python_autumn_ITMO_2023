def is_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


print(is_palindrome("radar"))
print(is_palindrome("level"))
print(is_palindrome("hello"))
print(is_palindrome(""))
print(is_palindrome("a"))
