class Solution:

    def convert_to_integer(self, s: str) -> int:
        number = 0

        for i in s:
            integer = (ord(i) - 48)
            digit = integer % 10
            number = number * 10 + digit

        return number

    def multiply(self, num1: str, num2: str) -> str:
        number1 = self.convert_to_integer(num1)
        number2 = self.convert_to_integer(num2)

        return str(number1 * number2)


obj = Solution()
num1 = '732'
num2 = '3'
print(obj.multiply(num1, num2))
