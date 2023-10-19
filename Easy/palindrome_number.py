class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reverse_num = 0

        while x > 0:
            remainder = x % 10
            reverse_num = reverse_num * 10 + remainder
            x //= 10

        return reverse_num == temp