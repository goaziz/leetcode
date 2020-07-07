

def isPalindrome(s):
    return [i for i in s.lower() if i.isalnum()] == [i for i in s[::-1].lower() if i.isalnum()]

d = 'ad'
print(isPalindrome(d))