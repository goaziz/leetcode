def isPalindrome(x):
    rev = 0
    t = x
    while x > 0:
        dig = x % 10
        rev = rev * 10 + dig
        x //= 10
    if rev == t:
        return True
    else:
        return False

print(isPalindrome(101))
